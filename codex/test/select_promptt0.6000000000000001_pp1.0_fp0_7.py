import select
# Test select.select()

import sys
import socket
import time

host = ''
port = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

def now():
    return time.ctime(time.time())

def handle_client(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data:
            break
        reply = 'Echo => %s at %s' % (data, now())
        connection.send(reply)
    connection.close()

def dispatcher():
    while True:
        connection, address = s.accept()
