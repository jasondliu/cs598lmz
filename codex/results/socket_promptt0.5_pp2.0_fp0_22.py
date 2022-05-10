import socket
# Test socket.if_indextoname()

print('\nTest 1:')
try:
    print(socket.if_indextoname(0))
except Exception as e:
    print(e)

print('\nTest 2:')
try:
    print(socket.if_indextoname(1))
except Exception as e:
    print(e)

print('\nTest 3:')
try:
    print(socket.if_indextoname('1'))
except Exception as e:
    print(e)

print('\nTest 4:')
try:
    print(socket.if_indextoname(2))
except Exception as e:
    print(e)

print('\nTest 5:')
try:
    print(socket.if_indextoname(3))
except Exception as e:
    print(e)

print('\nTest 6:')
try:
    print(socket.if_indextoname(4))
except Exception as e:
    print(e)

print('\nTest 7:')
try:
