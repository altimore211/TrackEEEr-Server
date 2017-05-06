import socket
import time
import json

client_name = raw_input("Enter client (trackEEEd) person here: ")

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('', 12360))

    ID = {}
    RSSIS = {}
    SSIDS = {}
    ID['id'] = client_name

    #Edit the next two lines for the actual data
    RSSIS['rssis'] = [-23, -61, -55, -62, -99]
    SSIDS['ssids'] = ['dilnet23', 'AccessPoint1', 'dilnet55', 'AccessPoint2', 'dilnet99']

    data = {key: value for (key, value) in (RSSIS.items() + ID.items() + SSIDS.items())}

    print data

    formatted_data = json.dumps(data)
    client.send(formatted_data)
    time.sleep(30) #pause 30 seconds before sending new data
