import socket
import sys
import time

_server = '192.168.0.10'
_port = 1337

_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_s.settimeout(4)

_s.connect((_server, _port))
_s.send('UserX\n')

data = _s.recv(1024)

if data.startswith('Welcome'):
    while True:
        data = _s.recv(1024)
        data = data.rstrip('\r\n')
        print data

        if data.startswith('Enter'):
            _s.send('%s\n' % str(int(time.time())))
            continue

        elif data.startswith('Good'):
            print 'Good job!'
            break

        _s.send('%s\n' % str(int(time.time())))

    _s.close()

else:
    print 'Protocol error'
    _s.close()

sys.
