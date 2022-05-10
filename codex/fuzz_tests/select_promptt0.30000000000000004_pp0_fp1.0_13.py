import select
# Test select.select()

def test_select():
    # Test select() on a simple readable socket.
    readable, writable, exceptional = select.select([sock], [], [], 0.0)
    if sock in readable:
        data = sock.recv(1024)
        if not data:
            break
        print(data)
