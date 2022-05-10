import socket
# Test socket.if_indextoname()
import os, string, sys, time
import select

def test_socket_if_indextoname():
    n_interfaces = 0
    for i in range(256):
        try:
            name = socket.if_indextoname(i)
            n_interfaces += 1
        except KeyError:
            pass
        else:
            #print 'Interface: %s index: %d' % (name, i)
            pass
    #print 'Test socket.if_indextoname() OK: %s interfaces were found' % n_interfaces


def test_select_error():
    r, w, e = select.select([1], [2], [3], 0.0)
    #print 'Test select() OK.'


def test_gaierror():
    try:
        socket.getaddrinfo('error.invalid', None)
    except socket.gaierror:
        #print 'Test gaierror() OK.'
        pass


