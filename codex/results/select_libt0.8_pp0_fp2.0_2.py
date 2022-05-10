import select
import socket
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python " + sys.argv[0] + " <PORT>"
        )
        sys.exit()
    
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('0.0.0.0', int(sys.argv[1])))
    server_sock.listen(5)

    while True:
        readable, writable, exceptional = select.select(
            [server_sock], [], []
        )
        for s in readable:
            if s is server_sock:
                client_sock, client_addr = s.accept()
                print(
                    "Client " + str(client_addr) + " connected"
                )
                client_s
