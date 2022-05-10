import socket
socket.if_indextoname(3)



# The most commonly used value is the default (0), which will turn on all of the 
# debugging flags. If you want to turn off all of the debugging flags, you can use 
# the value 99.

# The following two lines are equivalent and turn on all of the debugging flags:
socket.setdefaulttimeout(10)
socket.setdefaulttimeout(10.0)

# This line turns off all of the debugging flags:
socket.setdefaulttimeout(99)



# The socket module has many other constants and functions that you can use to
# configure sockets. For more information, see the socket module documentation.



# =============================================================================
#             Handling Exceptions (try and except)
# =============================================================================



# You can use the try statement to catch exceptions.
#
# The try statement has an optional finally clause that can be used for tasks that 
# should always be executed, whether an exception occurs or not. For example, to 
# always close a socket:

import socket
s = socket.socket()
try:
    s.connect(("www.python.org", 80))
