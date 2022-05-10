import socket
# Test socket.if_indextoname()

def main():
    for i in range(10):
        try:
            name = socket.if_indextoname(i)
        except ValueError:
            print('%d: no interface' % i)
        else:
            print('%d: %s' % (i, name))

if __name__ == '__main__':
    main()
