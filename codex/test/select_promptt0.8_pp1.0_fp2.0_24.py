import select
# Test select.select
import socket
import time

# delay = 5 # Delay in seconds
# while True:
#     r, w, e = select.select([sys.stdin], [], [], delay)
#     if not (r or w or e):
#         print('Nothing to do.')
#         break
#     if r:
#         print('Input ready:')
#         print(sys.stdin.readline())
#         break

def get_delay():
    return 5

def listen(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('localhost', port))
    s.listen(1)
    return s

def delay_accept(s):
    print('Delaying accept')
    r, w, e = select.select([s], [], [], get_delay())
    if s in r:
        print('Accepting')
