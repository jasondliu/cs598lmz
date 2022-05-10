import socket
import sys
import thread

## This is TCP receiver.

SERVER_IP = '127.0.0.1'
SERVER_PORT = 1300
BYTES = 1024
RUNNING = True


# Create receiver
receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print " *************************  "
print " ****** TCP RECEIVER ****** "
print " *************************  "
print " "
print " Connecting to ", SERVER_IP, " port: ", SERVER_PORT

receiver.connect((SERVER_IP, SERVER_PORT))


def receiver_server(threadName):
    global RUNNING
    global receiver
    global BYTES
    print "Server is running"

    while RUNNING:
        # Receive message from server
        data = receiver.recv(BYTES)

        if data:
            print "Message: ", data

        sleep(3)

    receiver.close()
    sys.exit()


### Main ######################################################################

# Initialize receiver
