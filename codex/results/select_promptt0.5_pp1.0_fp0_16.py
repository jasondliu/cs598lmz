import select
# Test select.select
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8080))
fd = sock.fileno()

print("send data")
sock.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

print("start select")
r, w, e = select.select([fd], [], [], 1)
print("select returned")

if r:
    data = sock.recv(1024)
    print("received: %s" % data)

print("close socket")
sock.close()

print("done")
