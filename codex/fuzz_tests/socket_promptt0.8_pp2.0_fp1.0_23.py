import socket
# Test socket.if_indextoname() raises OverflowError in case if the given index is
# out of range instead of returning an empty string.

def test(index):
    try:
        socket.if_indextoname(index)
        print('socket.if_indextoname({}) did not raise OverflowError'
              .format(index))
    except OverflowError:
        print('socket.if_indextoname({}) raised OverflowError'
              .format(index))

try:
    test(0)
    test(2**8-1)
    test(2**8)
    test(2**16-1)
    test(2**16)
    test(2**32-1)
except Exception as e:
    print('Unexpected exception:', e)
