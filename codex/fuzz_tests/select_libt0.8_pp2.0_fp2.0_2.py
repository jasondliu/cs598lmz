import select

print("Welcome to the Go server.")

sock_to_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_to_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_to_client.bind((socket.gethostname(), 12345))
sock_to_client.listen(5)
sock_to_client.setblocking(0)

sock_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_to_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_to_server.connect((socket.gethostname(), 54321))
sock_to_server.setblocking(0)

inputs = [sock_to_client, sock_to_server]
outputs = []

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs,
