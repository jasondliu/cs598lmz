import select
import sys
import os
import time

#initialize variables
data = ""
state = 0

#function to process data
def dataProcess(data):
    print(data)

#connect to the server
server = socket(AF_INET, SOCK_STREAM)
server.connect((sys.argv[1], int(sys.argv[2])))

#send the password
server.send(sys.argv[3])

#receive the login message
data = server.recv(1024)

if data == "Login successful":
    #receive the prompt
    data = server.recv(1024)
    print(data)
    state = 1

while True:
    try:
        [i,o,e] = select.select([server, sys.stdin], [], [])
    except select.error:
        break

    for s in i:
        if s == server:
            #receive data from server
            data = server.recv(1024)

            #check if server closed the connection
