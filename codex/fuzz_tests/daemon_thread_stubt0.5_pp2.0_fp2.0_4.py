import sys, threading

def run():
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        return
    port = int(sys.argv[1])
    print("Server listening on port %d" % port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", port))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        print("Connection from %s:%d" % addr)
        threading.Thread(target=handle_connection, args=(conn, addr)).start()

def handle_connection(conn, addr):
    while True:
        data = conn.recv(1024)
        if len(data) == 0:
            print("Connection from %s:%d closed" % addr)
            conn.close()
            return
        print("Received %d bytes: %s" % (len(data), data))
        conn.send(data)

if
