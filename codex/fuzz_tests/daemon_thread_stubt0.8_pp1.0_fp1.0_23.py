import sys, threading

def run():
    host="localhost"
    port=4000
    server = StreamServer((host, port), handle)
    server.serve_forever()

def handle(sock, addr):
    f = sock.makefile()
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        print >>sys.stderr, "got %r" % line

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    raw_input()
