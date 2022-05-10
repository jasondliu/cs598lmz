import select
# Test select.select(r, w, x)

# Create two sockets
s1, s2 = socket.socketpair()

print('Selecting on sockets')
for i in range(5):
    print(i)
    r, w, x = select.select([s1], [s2], [])
    print(r, w, x)
    if r:
        data = s1.recv(1)
        print('Received', repr(data), 'on', s1)
    if w:
        s2.send(b'*')
        print('Sent', '*', 'on', s2)
    assert not x

print('Closing one end')
s1.close()
for i in range(5):
    print(i)
    r, w, x = select.select([s2], [], [])
    print(r, w, x)
    if r:
        data = s2.recv(1)
        print('Received', repr(data), 'on', s2)
    assert not w
    assert not x

s2
