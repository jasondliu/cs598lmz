import socket
# Test socket.if_indextoname
def test(family):
    try:
        socket.if_indextoname(0, family)
    except ValueError as e:
        # Windows before Vista lacks this
        if e.args[0] != 'invalid argument':
            raise
        return False
    else:
        return True


from os.path import dirname, join as joinpath
from socket import socket, AF_PACKET, SOCK_DGRAM, SOL_SOCKET, SO_BINDTODEVICE, gaierror, error, timeout
from time import sleep
from errno import EADDRINUSE, EAGAIN
from subprocess import Popen
import sys
if test(AF_PACKET) or Popen(['ifconfig', 'lo:1', 'localhost']).wait():
    # Debian and FreeBSD share the same interface name
    # Windows and AIX are unsupported
    # Linux and Mac OS X are tested
    name = dirname(sys.argv[0])
    directory = joinpath(sys.prefix, 'Lib', 'test')
    path = joinpath(directory, name +
