import sys, threading

def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 2222))
    server.listen(10)
    while 1:
        conn, addr = server.accept()
        t = threading.Thread(target=worker, args=(conn,addr))
        t.start()

def worker(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send("ok\n")
        conn.close()
        break

if __name__ == '__main__':
    run()
