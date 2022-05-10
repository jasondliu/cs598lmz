import socket
# Test socket.if_indextoname() on linux.
# It's not supported on Windows.
if platform.system() == "Linux":
    # Test for valid inputs
    for i in range(0, 7):
        print socket.if_indextoname(i)

    # Test for invalid inputs
    print socket.if_indextoname(-1)
    print socket.if_indextoname(7)
