import socket
import time

PORT = 1234

def recieve_message(sock):
    data = ""
    try:
        data = sock.recv(1024)
        if data:
            return data
    except:
        pass
    return False

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', PORT))
    server_socket.listen(1)
    print "Server up and running"
    client_socket, client_address = server_socket.accept()
    print "Receiving data from ", client_address
    while True:
        data = recieve_message(client_socket)
        if data:
            print data

if __name__ == '__main__':
    main()
