import socket
import time

def main():
    
    #Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #Bind socket
    s.bind((socket.gethostname(), 1234))
    #Listen
    s.listen(5)
    #Accept connections
    (clientsocket, address) = s.accept()
    print(f"Connection from {address} has been established!")
    while True:
        #Receive data
        data = clientsocket.recv(1024)
        data = data.decode("utf-8")
        print(data)
        #Send data
        clientsocket.send(bytes("Hello from server", "utf-8"))
        time.sleep(1)
    #Close connection
    clientsocket.close()

if __name__ == "__main__":
    main()
