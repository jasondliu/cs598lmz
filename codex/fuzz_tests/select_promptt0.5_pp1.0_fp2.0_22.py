import select
# Test select.select()

import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen(5)

    while True:
        try:
            client_socket, addr = server_socket.accept()
        except KeyboardInterrupt:
            break
        else:
            print('Connection from', addr)

            # Make text-mode file wrappers for socket reading/writing
            client_socket.setblocking(False)
            client_socket.settimeout(5)
            client_socket.settimeout(None)
            client_socket.setblocking(True)
            client_socket.shutdown(socket.SHUT_RDWR)
            client_socket.close()

if __name__ == '__main__':
    server()
