import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

context = zmq.Context()
socket = context.socket(zmq.SUB)

# you can subscrive to more than one topic (use , to separate)
socket.setsockopt(zmq.SUBSCRIBE, "")
print "Collecting updates from weather server...\n"
socket.connect("tcp://192.168.123.115:5555")

# read from the socket!
while True:
    string = socket.recv()
    #print "left the socket"
    print "Received data is: %s" % string
