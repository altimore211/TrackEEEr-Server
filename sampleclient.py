import socket
import time

client_name = raw_input("Enter client (trackEEEd) person here: ")

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('', 12358))

    client.send(client_name)
    time.sleep(30) #pause 30 seconds before sending new data
