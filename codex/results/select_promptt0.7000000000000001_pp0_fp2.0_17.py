import select
# Test select.select()
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1], 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

while True:
    # Wait for input from stdin & socket
    try:
        inputs = [sys.stdin, sock]
        readable, writable, exceptional = select.select(inputs, [], [])
    except select.error, e:
        print >>sys.stderr, 'select.error:', e
        break
    except socket.error, e:
        print >>sys.stderr, 'socket.error:', e
        break
    except KeyboardInterrupt, e:
        print >>sys.stderr, 'keyboard interruption'
        break

    for s in readable:
        if s is sock:

