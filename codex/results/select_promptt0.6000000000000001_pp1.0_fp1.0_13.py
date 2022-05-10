import select
# Test select.select() with a socket object.
import socket
import time

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    s.listen(1)
    s.setblocking(0)
    print s.getsockname()
    c, addr = s.accept()
    print addr
    time.sleep(1)
    print 'selecting'
    r, w, x = select.select([c], [], [], 1.0)
    print 'selected'
    print r, w, x
    c.close()
    s.close()

if __name__ == '__main__':
    main()
