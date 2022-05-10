import select
import sys
import time
import random

HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    try:
        data = s.recv(1024)
        if data:
            print data
            if data == 'GAME OVER':
                break
    except socket.error:
        print 'Error Occured.\n'
        break

    if data == 'GAME START':
        time.sleep(random.randrange(1, 3))
        s.send('1')
    elif data == 'GO':
        time.sleep(random.randrange(1, 3))
        s.send('1')

s.close()
