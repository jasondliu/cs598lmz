import socket

host = ''
port = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

while True:
    print('Listening for connections...')
    
    client, addr = server.accept()
    print('Connection established with', addr)
    
    while True:
        data = client.recv(1024)
        reply = '[SERVER RECEIVED]>>>{}'.format(data.decode())
        
        if reply == -1:
            break
        else:
            print(reply)
            client.sendall(data)
    client.close()
server.close()
