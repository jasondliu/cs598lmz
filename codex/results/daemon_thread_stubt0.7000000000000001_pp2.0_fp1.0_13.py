import sys, threading

def run():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', int(sys.argv[1])))
        server.listen(1)
        conn, addr = server.accept()
        try:
            print('connected')
            buf = b''
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                buf += data
                print(buf)
        finally:
            conn.close()
    finally:
        server.close()

thread = threading.Thread(target=run)
thread.start()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', int(sys.argv[1])))
s.sendall(b'hello')
s.close()

thread.join()
</code>

