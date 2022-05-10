import selectors
import socket
import types

#server_address = ('localhost', 10000)
#print('starting up on {} port {}'.format(*server_address))
#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#server.bind(server_address)
#server.listen(5)
#server.setblocking(False)
#
#sel = selectors.DefaultSelector()
#sel.register(server, selectors.EVENT_READ, data=None)
#
#try:
#    while True:
#        events = sel.select(timeout=None)
#        for key, mask in events:
#            if key.data is None:
#                accept_wrapper(key.fileobj)
#            else:
#                service_connection(key, mask)
#except KeyboardInterrupt:
#    print('caught keyboard interrupt, exiting')
#finally:
#    sel.close()

