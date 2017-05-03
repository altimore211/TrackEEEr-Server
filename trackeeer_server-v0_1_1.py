#   First trial for TrackEEEr Server
#       Notes:
#        a. To make sqlite3 database, install via "sudo apt-get install sqlite"
#        b. Make database by "sqlite3 trackeeer"
#        c. Create table by "sqlite> CREATE TABLE trackeeed (mac_addr text, desc text, gen_location text, last_update text);"
#
#       Not yet tested; simple framework

#   02/05/17 - Added socket communication functionality

from datetime import datetime
import time
import sqlite3
import socket
import signal
import sys

#   Define the server address; configured to listen to any address attached to the server and an arbitrary port
serverAddress = ('', 12345)
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

db = sqlite3.connect('trackeeer.db')

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
            #Parsing of Data - Lea
            #Finding out general location - Enzo
#            ssid = data_dict['SSID']
#            user = data_dict['USER']
#            mac_addr = data_dict['MAC']
#            desc = data_dict['DESC']
#            gen_location = data_dict['LOCATION']
            last_update = str(datetime.now())

            #Inserts new row of data
#            cursor.execute("INSERT INTO trackeeed VALUES ('','','','')") #blank values for now (variable data)
            db.commit()
            print data #check received data (Debugging purposes)
        else:
            print "Failed to get any new data."



    #end
    db.close()

if __name__ == "__main__":
	print ("-Server-")
	main()
