import socket
import subprocess

serverIP = "127.0.0.1"
serverPort = 12347

# creating the server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binding the the IP address and port with the server socket
serverSocket.bind((serverIP, serverPort))
print("Server started")
while True:
    # listening for connections
    serverSocket.listen(1)
    print("Server listening for connections")
    # accepting the connection
    connectionSocket, addr = serverSocket.accept()
    print("Connection accepted from", addr)
    
    while True:
        # recieving command from client
        command = connectionSocket.recv(1024)
        command = command.decode("utf-8")
        if command == "exit" or command == "quit":
            break
        print("CLient sent command:", command)
        # running the command in terminal and capturing the output
        result = subprocess.check_output(command, shell=True)
        result = result.decode("utf-8")
       
