import select
# Test select.select
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Server is ready to receive")

while True:
    # wait for next request, then receive and print
    readable, writable, exceptional = select.select([serverSocket], [], [], 0.5)
    if len(readable) > 0:
        message, clientAddr = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper().encode()
        serverSocket.sendto(modifiedMessage, clientAddr)
