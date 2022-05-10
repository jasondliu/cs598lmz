import socket
from contextlib import closing

def main():
    host = '127.0.0.1'
    port = 4000
    bufsize = 4096
    buf = ''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with closing(sock):
        sock.bind((host, port))
        sock.listen(1)
        conn, addr = sock.accept()
        with closing(conn):
            while True:
                conn.send('HTTP/1.0 200 OK\r\n\r\n')
                while len(buf) < 4:
                    buf += conn.recv(bufsize)
                if buf == '':
                    break
                length = int(buf)
                buf = buf[4:]
                size = 0
                while size < length:
                    block = length - size
                    if block > bufsize:
                        block = bufsize
                    tmp = conn.recv(block)
                    size += len(tmp)
                    buf += tmp
                if buf == '':
                    break
                f = open("
