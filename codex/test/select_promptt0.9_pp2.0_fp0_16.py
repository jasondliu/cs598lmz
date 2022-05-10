import select
# Test select.select function:
# Run this program, type some lines, then type ^D.  Select is used to tell
# if there is input ready on stdin, if data is ready to be read from test
# socket, and if stdout file is ready for more output.
# Look at module select for other useful select functions.
#
# Usage example:
#   % ./test_select.py 5051
#   Starting test at Mon Oct  7 19:09:21...
#   Input:  hello
#   Input to socket:  hello
#   Input:  world
#   Input to socket:  world
#   Input:  ^D
#
# Caveat: DOS box: must use Ctrl+Z for EOF, not Ctrl+D

# Create a simple test server
#
# Caveat: OS X: must use 127.0.0.1 instead of localhost
HOST = 'localhost'               # Symbolic name meaning the local host
PORT = 0                        # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
