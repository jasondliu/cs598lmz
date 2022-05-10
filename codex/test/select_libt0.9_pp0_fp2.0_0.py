import select
import os
import time
import sys

server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind('/dev/stdout')
#client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
#client.bind('/home/a.out')
#client.connect('/home/a.out') #name the stat file the same thing as the program

while True:
    try:
        message = server.recv(100000) #theoretically big enough for any chat message
        print(f'{os.getpid()} says: {message}')
    except KeyboardInterrupt:
        #print(client.recv(100))
        print(os.getpid(), 'is killin')
        client.close()
