import threading
threading.stack_size(128*1024)

def send_to_server(client_socket, send_data):
    #print("send_to_server")
    #print(send_data)
    client_socket.sendall(json.dumps(send_data).encode())


def receive_from_server(client_socket):
    #print("receive_from_server")
    recv_data = client_socket.recv(1024).decode()
    #print(recv_data)
    recv_data = json.loads(recv_data)
    return recv_data

def send_receive_from_server(client_socket, send_data):
    #print("send_receive_from_server")
    send_to_server(client_socket, send_data)
    recv_data = receive_from_server(client_socket)
    return recv_data

