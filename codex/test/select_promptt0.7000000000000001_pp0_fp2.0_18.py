import select
# Test select.select()
#
# Can we handle a fd which is not a socket?
#

import socket
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.bind (('', 0))
s.listen (1)

#
# Read a byte from a socket, but don't consume it
#
def read_byte (s):
    r, w, e = select.select ([s], [], [], 0)
    if s in r:
        return s.recv (1, socket.MSG_PEEK)
    return None

#
# Accept a connection, but don't consume it
#
def accept_connection (s):
    r, w, e = select.select ([s], [], [], 0)
    if s in r:
        return s.accept ()
    return None
    

#
# We just do the initial accept, but don't consume it
#
conn, addr = accept_connection (s)
assert conn != None

#
# We can't read the character yet, because the connection is

