import socket

class Client(asyncio.Protocol):
    # Callback that handles successful connection to the server and
    # initializes the client with the server's IP and port
    def connection_made(self, transport):
        self.server_ip = transport.get_extra_info('peername')[0]
        self.server_port = transport.get_extra_info('peername')[1]
        self.transport = transport

    # Callback that handles data sent from the server
    def data_received(self, data):
        print(data.decode())

    def connection_lost(self, exc):
        print("Disconnected from server")
        self.transport.close()

def print_usage():
    print("Usage: ./client.py [IP] [PORT] [USERNAME]")

def main(argv):
    if len(argv) < 4:
        print_usage()
        sys.exit()

    ip = argv[1]
    port = argv[2]
    username = argv[3]

    loop = asyncio
