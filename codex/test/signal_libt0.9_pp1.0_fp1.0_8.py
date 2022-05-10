import signal
signal.signal(signal.SIGINT, handler)

def recv(c_socket):
    while True:
        try:
            data = c_socket.recv(1024)
            if not data:
                print("Closing socket")
                c_socket.close()
                break
            print(data.decode("utf-8"))
        except:
            pass

def send(c_socket):
    while True:
        c_socket.sendall(input("Enter message: ").encode("utf-8"))

def main():
    global c_socket
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect((socket.gethostname(), 9999))
    print("Connection Established")
    thread_recv = threading.Thread(target=recv, args=(c_socket,))
    thread_recv.start()
    thread_send = threading.Thread(target=send, args=(c_socket,))
    thread_send.start()

