import socket
import time

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('', 12345))

    client.send('Sample data sent.')
    time.sleep(30) #pause 30 seconds before sending new data
