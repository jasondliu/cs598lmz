import signal
signal.signal(signal.SIGINT, signal_handler)

def main():
    if len(sys.argv) != 2:
        print 'Usage: %s HOST' % sys.argv[0]
        return 1

    addr = sys.argv[1].split(':')
    if len(addr) != 2:
        print 'Usage: %s HOST' % sys.argv[0]
        return 1

    addr[1] = int(addr[1])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((addr[0], addr[1]))
    print "connect to %s:%d" % (addr[0], addr[1])

    # connect
    msg = 'HELLO-FROM-CLIENT'
    sock.send(msg)
    print "send message: %s" % msg

    # recv hello
    try:
        msg = sock.recv(1024)
        print "recv message: %s" % msg
    except socket.
