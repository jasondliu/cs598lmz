import socket

def main():
    host = '127.0.0.1'
    port = 5000
    
    s = socket.socket()
    s.connect((host, port))
    
    message = input("Enter data: ")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024)
        print("Received from server: " + str(data.decode()))
        
        message = input("Enter data: ")
    s.close()

if __name__ == "__main__":
    main()
