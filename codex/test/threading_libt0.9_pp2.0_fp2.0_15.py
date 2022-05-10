import threading
threading.stack_size(0x500000)  # set thread stack

# Create the server, binding to localhost on port 9999
class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass
server = ThreadedUDPServer(("localhost", 9999), ThreadedUDPRequestHandler)

# Activate the server; this will keep running until you
# interrupt the program with Ctrl-C
server.serve_forever()
