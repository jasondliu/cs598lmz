import socket
# Test socket.if_indextoname()
import socket
for s in socket.if_nameindex():
    if s[1] == 'lo':
        print(s[0])
        break
else:
    raise RuntimeError("No loopback device found")

# Create a server socket
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1234))
s.listen(1)
print('Listening at', s.getsockname())
while True:
    sc, sockname = s.accept()
    print('Processing up to 1024 bytes at a time from', sockname)
    n = 0
    while True:
        message = sc.recv(1024)
        if not message:
            break
        sc.sendall(message)
        n += len(message)
        print('\r  %d bytes processed so far' % (n,), end=' ')
        sys.stdout.flush()
    print()
    sc.close()
    print('  Socket closed')

# Create a server socket
import socket
