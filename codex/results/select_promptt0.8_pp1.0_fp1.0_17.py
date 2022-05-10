import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.2)

# Start a socket server, with no connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 15000))
server.listen(10)

# Pretend we're doing some blocking activity
start = time.time()
for _ in range(5):
    slow_systemcall()
# How long did that take?
duration = time.time() - start  # Around 1 second
print(duration)

# Start a socket server, with a client connecting
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 15000))
server.listen(10)

client = socket.socket(socket.AF_
