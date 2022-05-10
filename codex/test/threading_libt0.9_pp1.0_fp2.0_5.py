import threading
threading.stack_size(4096 * 1024)

# Implementing the client-side of the UDP connection
# --------------------------------------------------
HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 42069              # Arbitrary non-privileged port

# The following functions are defined to be used in a thread's execution.
def sendMessage(s, message):
    s.sendto(message, (HOST, PORT))
