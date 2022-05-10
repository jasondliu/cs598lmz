import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    '''
    This function tests socket.if_indextoname()
    '''
    i = 0
    for if_name in socket.if_indextoname(i):
        i += 1
        print(if_name)

def test_if_indextoname_err():
    '''
    This function tests socket.if_indextoname()
    '''
    try:
        socket.if_indextoname(0)
    except socket.error:
        pass
    else:
        print("Error: %s" % str(socket.error))
