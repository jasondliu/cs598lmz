import select
# Test select.select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
server.setblocking(0)
server.bind(('localhost', 50000))
server.listen(1)

connections = {}
readers = [server]
writers = []

while readers:
    readable, writable, exceptional = select.select(readers, writers, readers)

