import select
# Test select.select() with a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))
print(select.select([sock], [], []))
# Test select.select() with a file
f = open('/dev/null')
print(select.select([f], [], []))
# Test select.select() with a socket, file and pipe
r, w, x = select.select([sock, f], [], [])
print(r)
print(f in r)
print(sock in r)
# Test select.select() with a socket and a file with timeout
print(select.select([sock, f], [], [], 1))
# Test select.select() with a socket, a file and a pipe with timeout
r, w, x = select.select([sock, f], [], [], 1)
print(r)
print(f in r)
print(sock in r)
# Test select.poll() with a socket
p = select.poll()
p.register(
