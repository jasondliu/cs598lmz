import socket
# Test socket.if_indextoname()
if_indextoname = socket.if_indextoname

def test_if_indextoname(index):
    print(if_indextoname(index))

if __name__ == '__main__':
    test_if_indextoname(1)
