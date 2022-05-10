import sys, threading

def run():
    global clientSocket
    # The server's hostname or IP address
    HOST = 'localhost'
    # The server's port
    PORT = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        clientSocket = s
        #s.sendall(b'Hello, world')
        #data = s.recv(1024)
        #print('Received', repr(data))

        while True:
            msg = input("> ")
            if msg == "exit":
                return
            s.sendall(msg.encode('utf-8'))
            data = s.recv(1024)
            print('Received', repr(data))

def send_msg(message):
    clientSocket.sendall(message.encode('utf-8'))

if __name__ == "__main__":
    #sys.exit(run())
    t1 = threading.Thread(target=run)
    t1.start()

    print("
