import threading
threading.stack_size(4096 * 1024)

# Implementing the client-side of the UDP connection
# --------------------------------------------------
HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 42069              # Arbitrary non-privileged port

# The following functions are defined to be used in a thread's execution.
def sendMessage(s, message):
    s.sendto(message, (HOST, PORT))
    print 'Message Sent:', message
    reply, addr = s.recvfrom(4096)
    print 'Message Receieved:', reply

def getIP(s):
    s.sendto('!IP', (HOST, PORT))
    reply, addr = s.recvfrom(4096)
    print addr[0]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Here is where a UDP connection is established
# ---------------------------------------------

# One thread to send UDP messages
thread1 = threading.Thread(target=sendMessage, args=(s, 'Hello World:',))


