import socket
# Test socket.if_indextoname() with an unused interface
try:
    socket.if_indextoname(1)
except socket.error as e:
    if e.errno != errno.EINVAL:
        # This can occur on Windows, in which case it is a
        # known failure, so do nothing
        pass
except NameError:
    # Probably IPv6 is not available
    pass

# Test the use of : in the server address.
try:
    socket.getaddrinfo(socket.gethostname(),
                       SMTPHandler.defaults['mailport'])
except socket.gaierror:
    # This can occur on Windows, in which case it is a
    # known failure, so do nothing
    pass
finally:
    # If this fails, it is a problem inside getaddrinfo,
    # so that's a different problem than we're trying to
    # verify here.
    socket.getaddrinfo(socket.gethostname() + ':')


@unittest.skipUnless(hasattr(signal, 'SIGALRM'), 'Need signal module with SIGALRM')
