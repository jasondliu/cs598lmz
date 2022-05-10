import socket
# Test socket.if_indextoname()

if __name__ == '__main__':
    for i in range(0, 100):
        try:
            name = socket.if_indextoname(i)
            print("%d: %s" % (i, name))
        except:
            pass
