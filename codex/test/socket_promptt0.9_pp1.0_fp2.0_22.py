import socket
# Test socket.if_indextoname function
try:
    socket.if_indextoname(2)
except:
    pass

socket.if_indextoname(203087)

test('O')

test('q', hex=False, wide=True)
test('a', hex=False, wide=True)
test('\0', hex=True, wide=True)
test('\0', hex=True, wide=False)
test('ab', hex=True, wide=False)

test('a', hex=True, wide=False)
test('ab', hex=True, wide=False)
test('abc', hex=True, wide=False)

test('MySQL')
test('a\0b')
test('a\0\0b')
test('a\0\0b\0cd')
test('a\0\0b\0cd\0')

