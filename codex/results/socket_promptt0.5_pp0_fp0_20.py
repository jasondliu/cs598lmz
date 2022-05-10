import socket
# Test socket.if_indextoname()
#
# Tested on:
# Debian 8.8
# Ubuntu 16.04.2
#
# Example:
# $ python if_indextoname.py
#
# Output:
# if_indextoname() returned: lo
#
# The above output means that the function returned 'lo' which is the name
# of the loopback interface.

if __name__ == '__main__':
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Get the interface index of the loopback interface
    index = s.if_nametoindex('lo')
    # Get the name of the interface corresponding to the index
    name = socket.if_indextoname(index)
    # Print the name
    print "if_indextoname() returned: " + name
