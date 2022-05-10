import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Get the interface index of the loopback interface
    index = s.if_nametoindex('lo')

    # Get the name of the loopback interface
    name = s.if_indextoname(index)

    # Check if the name is the same as the one we used to get the index
    if name == 'lo':
        print('Success')
    else:
        print('Failed')

