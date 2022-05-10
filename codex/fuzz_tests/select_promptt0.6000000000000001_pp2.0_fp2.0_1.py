import select
# Test select.select()
#
# Create a pair of connected sockets
import socket

def test():
    s1, s2 = socket.socketpair()
    for i in range(5):
        print 'PASS'
        # select should always return immediately since the sockets are
        # connected.
        r, w, x = select.select([s1], [s2], [], 1.0)
        #print 'r =', r
        #print 'w =', w
        #print 'x =', x
        if r:
            #print 'r =', r
            if s1 in r:
                data = s1.recv(1024)
                #print 'Received', repr(data)
                if not data:
                    #print '  closing', s1
                    s1.close()
                else:
                    #print '  sending', repr(data), 'to', s2
                    s2.send(data)
        if w:
            #print 'w =', w
            if s2 in w:
                #print '  sending to', s2
                s2.send('
