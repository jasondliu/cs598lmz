import select
# Test select.select()

# How long to wait for a response from a server
timeout = 5

# Create two sockets
socks = []
for res in socket.getaddrinfo("www.google.com", 80, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    socks.append(s)

# How many sockets are ready to be read
# timeout is how long to wait for a response from a server
# before giving up
ready = select.select(socks, [], [], timeout)[0]

# Print which sockets are ready to be read
for s in ready:
    print(s.getpeername())
    s.sendall(b'GET / HTTP/1.1\r\n')
    s
