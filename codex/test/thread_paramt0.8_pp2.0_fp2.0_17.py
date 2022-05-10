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
