import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

'''

# send method2
'''
import sys, socket, select
sock = socket.create_connection(('localhost', 9991))
while True:
    read_fds, _, _ = select.select([sys.stdin, sock], [], [], 1)
    if sys.stdin in read_fds:
        sock.send(sys.stdin.read())
    if sock in read_fds:
        print sock.recv(4096)
'''

# recv
'''
import sys, socket, select
sock = socket.create_connection(('localhost', 9991))
def recv_all(sock):
    data = ''
    while True:
        d = sock.recv(4096)
        if not d: break
        data += d
    return data
while True:
    read_fds, _, _ = select.select([sys.stdin, sock], [], [], 1)
    if sys.stdin in read
