import select
# Test select.select()
from socket import socket, AF_INET, SOCK_STREAM
import sys
from time import sleep

sys.stdout = open('_testout', 'w')
port = 50008
host = 'localhost'

def now():
    return time.ctime(time.time())

def all_events():
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind(('', port))
    serversock.listen(5)
    serversock.setblocking(0)
    event_list = [serversock]
    while True:
        print('\npolling for events at:', now())
        readable, writable, exceptional = select.select(event_list, [], [])
        for sockobj in readable:
            if sockobj is serversock:
                connection, address = sockobj.accept()
                print('server', address, end='')
                connection.setblocking(0)
                event_list.append(connection)
            else:
                data = sockobj.recv(1024)
                print
