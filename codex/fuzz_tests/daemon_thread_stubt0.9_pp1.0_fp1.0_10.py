import sys, threading

def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()
    s.close()
    return ip[0]

N = 2

server = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
port = int(sys.argv[2]) if len(sys.argv) > 2 else 8820

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        sock.connect((server, port))
        break
    except socket.error:
        sleep(5)
        print "Connecing..."

def recv():
    while True:
        data = sock.recv(1024)
        if not data:
            sys.exit(0)
        sys.stdout.write(data)

t = threading.Thread(target=recv)
t.
