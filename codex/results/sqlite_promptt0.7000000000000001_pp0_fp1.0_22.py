import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/pi/test.db')

libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.prctl(1, 15)

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 10000))
server_socket.listen(1)

def process_request(conn):
    data = conn.recv(512)
    if not data:
        return
    conn.sendall(data)


def worker():
    while True:
        conn, addr = server_socket.accept()
        process_request(conn)
        conn.close()


workers_count = 10
for i in xrange(workers_count):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

while True:
    time.sleep(1)
</code>
What I've found out

I've tried to print the pid and the socket file descriptor, and found that the process is never restarted (it's the same process).
