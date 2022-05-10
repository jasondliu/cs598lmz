import sys, threading

def run():
    while 1:
        msg = sock.recv(1024)
        if msg:
            sys.stdout.write(msg)
            sys.stdout.flush()
        else:
            break

def send():
    while 1:
        msg = sys.stdin.readline()
        if msg:
            sock.send(msg)
            sys.stdout.flush()
        else:
            break

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'usage: client.py <host> <port>'
        sys.exit(2)

    host = sys.argv[1]
    port = int(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    r = threading.Thread(target=run)
    r.start()
    s = threading.Thread(target=send)
    s.start()
