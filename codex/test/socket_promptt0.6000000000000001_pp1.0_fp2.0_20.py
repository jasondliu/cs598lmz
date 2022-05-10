import socket
# Test socket.if_indextoname()

def test(args=[]):
    for i in range(0, 10):
        try:
            print(socket.if_indextoname(i))
        except:
            pass

if __name__ == "__main__":
    test()
