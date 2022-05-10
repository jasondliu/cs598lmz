import select
# Test select.select()

def run_select(sock):
    while True:
        rlist, wlist, xlist = select.select([sock], [], [])
        print "rlist:", rlist
        if rlist:
            data = sock.recv(1024)
            if not data:
                break
            print "received:", data

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 25000))

run_select(sock)
