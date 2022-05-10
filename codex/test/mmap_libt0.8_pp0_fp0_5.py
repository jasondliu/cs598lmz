import mmap
import sys

def send_recv(data):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('localhost', 9000))
    conn.send(data)
    conn.setblocking(0)
    try:
        return conn.recv(1024)
    except:
        return None

