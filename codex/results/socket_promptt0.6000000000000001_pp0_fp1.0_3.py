import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    index = socket.if_nametoindex('lo')
    name = socket.if_indextoname(index)
    print(index, name)
    assert name == 'lo'

if __name__ == '__main__':
    test_if_indextoname()
