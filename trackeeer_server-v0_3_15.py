#   TrackEEEr Server
#       Notes:
#        a. To make sqlite3 database, install via "sudo apt-get install sqlite"
#        b. Make database by "sqlite3 trackeeer"
#        c. Create table by "sqlite> CREATE TABLE trackeeed (tracked_user text, desc text, gen_location text, last_update text);"
#        d. Don't forget to exit by inputting "sqlite> .quit"
#
#       Update (May 05 2017) - Tested with sampleclient.py and dummy data. Works.

#   May 02 2017 - Added socket communication functionality
#   May 05 2017 - Added filtering of data received and max RSSI detection
#   May 06 2017 - Added parsing of json object and database update

from datetime import datetime
import time
import sqlite3
import socket
import signal
import sys
import json
import os.path
#   Define the server address; configured to listen to any address attached to the server and an arbitrary port
serverAddress = ('', 12360)
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(directory, 'trackeeer.db')
db = sqlite3.connect(database_path)

#   Handles shutdown by Ctrl+C
def sig_handler(signum, frame):
    print "SERVER CLOSED\n"
    serverSock.close()
    db.close()
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, sig_handler)

    serverSock.bind(serverAddress)
    serverSock.listen(5)

    while True:
        cursor = db.cursor()

        #Accept and receive data from client
        conn, client_address = serverSock.accept()
        data = conn.recv(1024)

        if data:
            #parse json data
            j = json.loads(data)

            ID = j['id']
            received_SSIDS = j['ssids']
            received_RSSIS = j['rssis']
            faculty = 'UCL'

            print ID, "has connected." #check client that connected (Debugging purposes)

            last_update = str(datetime.now())

            SSIDS = []
            RSSIS = []
            access_pt = 0 #Checks if close to multiple access points

            #Removes trash data (Non access point data)
            remove_counter = 0
            for j in received_SSIDS:
                if "AccessPoint" in j:
                    SSIDS.append(j)
                    RSSIS.append(received_RSSIS[remove_counter])
                remove_counter += 1

            m = max(RSSIS)
            i = 0
            ctr = 0

            #Prints out the closest access point relative to the device connected.
            for i in RSSIS:
                if i == m:
                    print SSIDS[ctr]
                    gen_location = SSIDS[ctr] #general location is for now temporarily set as the SSID

                    access_pt += 1
                    ctr += 1
                    continue
                ctr += 1

            if access_pt > 1:
                print "The person is close to these multiple access points."
                #In the occasion that access points have the same rrsi
            else:
                print "The person is close to this access point."

            print "INSERT INTO trackeeed VALUES ('%s','%s','%s','%s')" % (ID, faculty, gen_location, last_update)
            #Inserts new row of data
            cursor.execute("INSERT INTO trackeeed VALUES ('%s','%s','%s','%s')" % (ID, faculty, gen_location, last_update))
            db.commit()
        else:
            print "Failed to get any new data."

    #end
    db.close()

if __name__ == "__main__":
	print ("-Server-")
	main()
