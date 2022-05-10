import sys, threading

def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 80))
    server_socket.listen(5)

    while True:
        (client_socket, address) = server_socket.accept()
        client_thread = threading.Thread(target = serve_client, args = (client_socket, address))
        client_thread.start()

def serve_client(client_socket, address):
    request = client_socket.recv(1024)
    print(request)
    response = http_handle.handle_request(request)
    client_socket.send(response)
    client_socket.close()

run()
