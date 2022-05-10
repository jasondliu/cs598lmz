import select
# Test select.select function.
# Use select.select() to monitor multiple sockets for data arrival
# simultaneously.

# create two sockets
s1 = socket.socket()
s2 = socket.socket()
s1.connect(("localhost", 8001))
s2.connect(("localhost", 8002))

while True:
    readable_sockets, _, _ = select.select([s1, s2], [], [])
    assert len(readable_sockets) > 0
    readable_socket = readable_sockets[0]
    if readable_socket is s1:
        print("s1")
        print(s1.recv(1024))
    elif readable_socket is s2:
        print("s2")
        print(s2.recv(1024))
