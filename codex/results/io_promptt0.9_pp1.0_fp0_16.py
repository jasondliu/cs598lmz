import io
# Test io.RawIOBase.readintoall() with a regular file
a = io.RawIOBase().readintoall(str(make_script("return 42")))
total = 0
for chunk in a:
    total += sum(chunk)
assert total == 42

# Test io.RawIOBase.readintoall() with a socket
client, server = socket.socketpair()
for i in range(100):
    client.sendall(b"x" * i)

def readintoall(timeout):
    return io.RawIOBase().readintoall(client)

with timeouts(.1, readintoall) as a:
    total = 0
    for chunk in a:
        total += len(chunk)
    assert total == sum(range(100))
