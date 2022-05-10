import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_index = 3
    if_name = socket.if_indextoname(if_index)
    print('if_index: %d, if_name: %s' % (if_index, if_name))
    if_index = 10
    if_name = socket.if_indextoname(if_index)
    print('if_index: %d, if_name: %s' % (if_index, if_name))

# Test socket.if_nameindex()

def test_if_nameindex():
    if_nameindex = socket.if_nameindex()
    print('if_nameindex:')
    for if_index, if_name in if_nameindex:
        print('%d: %s' % (if_index, if_name))

# Test socket.if_nametoindex()

def test_if_nametoindex():
    if_name = 'eth0'
    if_index = socket.if_nametoindex(if_name)
   
