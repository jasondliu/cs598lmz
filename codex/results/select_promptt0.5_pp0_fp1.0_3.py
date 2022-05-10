import select
# Test select.select()

import socket
import time
import select


def test_select():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 5000))
    s.listen(10)

    while True:
        inputready, outputready, exceptready = select.select([s], [], [])
        if inputready:
            print 'Got a connection!'
            connection, client_address = s.accept()
            print '    from ', client_address
            while True:
                data = connection.recv(16)
                print '    received "%s"' % data
                if data:
                    print '    sending data back to the client'
                    connection.sendall(data)
                else:
                    print '    no more data from', client_address
                    break
            connection.close()

# Test select.poll()

import select
import socket
import time

def test_poll():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM
