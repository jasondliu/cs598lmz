import selectors
import sys

HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 9009

def chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
    print 'Chat server started on port : ' + str(PORT)
    
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)
    
    while True:
        # get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(SOCKET_LIST,[],[])
        for sock in read_sockets:
            # a new connection request recieved
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
