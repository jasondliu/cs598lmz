import sys, threading

def run():
    args = sys.argv
    if len(args) < 2:
        print "usage: python2.7 %s <port>" % args[0]
        sys.exit(-1)

    port = int(args[1])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print "Connection from %s:%d" % (addr[0], addr[1])
        threading.Thread(target=handle_client, args=(conn, addr)).start()

def handle_client(conn, addr):
    data = conn.recv(1024)
    print data
    conn.send(data)
    conn.close()

if __name__ == '__main__':
    run()
