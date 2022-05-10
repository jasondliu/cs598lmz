import select
# Test select.select() using a timeout
import time

print("This program requires user input on both stdin and stdout")
print("Please ensure that you are using both input and output channels")
print("Otherwise the program will hang")

# Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set some options to make it easier to test
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(5)

# Bind to the interface and port
s.bind(("0.0.0.0", 10000))

# Create a readable file object that can be passed
# to a select call
f = s.makefile("r")

# Loop until the user enters a blank line
while True:
    # Wait for input from stdin
    # or until the socket is ready
    readable, writable, errored = select.select([f, sys.stdin], [], [])
    for s in readable:
        # See if there is data on the socket
       
