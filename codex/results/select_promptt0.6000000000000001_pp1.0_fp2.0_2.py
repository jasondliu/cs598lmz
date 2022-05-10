import select
# Test select.select() to wait for socket status change
#
# Usage:
#    python select_test.py
#
# The program will display a list of sockets and a list of
# interesting events.  It will then wait for one of the sockets
# to experience an event in the list.
#
# To exit the program, type a Control-C

# Use the name of the local host
host = ''

# Create two sockets
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associate the sockets with files
f1 = s1.makefile('w', 0)
f2 = s2.makefile('w', 0)

# Bind the sockets to random ports
s1.bind((host, 0))
s2.bind((host, 0))

# Display the port numbers
print 'socket 1:', s1.getsockname()
print 'socket 2:', s2.getsockname()

# Wait for events
while True:
   
