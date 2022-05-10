import selectors
import time
import sys

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def event_loop(sel, sock, fib_n):
    data = sys.stdin.readline()
    print('\n----\n', data)
    n = int(data)
    sel.get_map()[sock].send(str(n).encode('ascii'))
    res = fib_n(n)
    sock.send(b'%d' % res)

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
