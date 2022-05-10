import socket
# Test socket.if_indextoname()
#
# This test checks that if_indextoname() raises a ValueError when given a
# non-existent interface index.

if __name__ == '__main__':
    print(socket.if_indextoname(0))
    try:
        socket.if_indextoname(999999)
    except ValueError:
        print('ValueError')
    else:
        print('no ValueError')
