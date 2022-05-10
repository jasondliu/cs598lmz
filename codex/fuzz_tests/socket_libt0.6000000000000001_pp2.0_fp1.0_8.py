import socket
import sys

def usage():
    print "Usage: python %s <port>" % sys.argv[0]
    exit(1)

def main():
    if len(sys.argv) != 2:
        usage()

    port = int(sys.argv[1])

    with socket.socket() as s:
        s.bind(('', port))
        s.listen(1)

        print "Listening on port %d..." % port
        conn, addr = s.accept()

        print "Accepted connection from %s:%d" % addr
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    print "Client disconnected"
                    break
                print "Received: %s" % data
                conn.send(data)


if __name__ == '__main__':
    main()
