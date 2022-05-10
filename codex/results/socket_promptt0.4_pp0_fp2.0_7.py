import socket
# Test socket.if_indextoname()
#
# This test is expected to fail if the system does not have a network
# interface named "lo".

if_indextoname = socket.if_indextoname

if not hasattr(socket, 'if_indextoname'):
    print('if_indextoname not found')
else:
    try:
        print(if_indextoname(1))
    except OSError as e:
        if e.errno == errno.ENXIO:
            print('SKIP')
        else:
            raise
