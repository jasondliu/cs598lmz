import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    for i in range(100):
        try:
            socket.if_indextoname(i)
        except ValueError:
            pass
        else:
            break
    else:
        raise Exception("can not find a valid interface")

if __name__ == '__main__':
    test_if_indextoname()
