import socket
import sys
import threading
import time

s = None

def server():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 3333))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
    conn.close()

thread = threading.Thread(target=server)
thread.start()

time.sleep(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 3333))
s.send('Hello world')
s.close()

thread.join()

# vim: tabstop=4 expandtab shift
