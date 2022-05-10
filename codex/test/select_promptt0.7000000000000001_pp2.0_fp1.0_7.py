import select
# Test select.select()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 5000))
sock.setblocking(0)

poller = select.poll()
poller.register(sock.fileno(), select.POLLIN)

while True:
    print('Checking...')
    events = poller.poll(2000)
