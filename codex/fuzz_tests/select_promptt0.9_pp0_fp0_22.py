import select
# Test select.select() on a allready connected socket.

import os, sys, select, socket

port =    55555

python = sys.executable
prog = os.path.realpath(sys.argv[0])
script = os.path.join(os.path.dirname(prog), 'accept_test2.py')

if 'SOCK_STREAM' not in dir(socket):
    raise SystemExit('socket.SOCK_STREAM not defined')

addr = 'localhost', port
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.bind(addr)
tcpsock.listen(1)

r, w, e = select.select([tcpsock], [], [], 5.0)
if tcpsock not in r:
    raise SystemExit, 'Socket not ready for reading: %s' % (tcpsock,)

a, b = os.popen2(python, 'b')
a.write('%s\n' % (port,))
a.flush()


