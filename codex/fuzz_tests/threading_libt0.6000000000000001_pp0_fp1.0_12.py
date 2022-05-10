import threading
threading.stack_size(67108864)



def main():
    print("Starting the server...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    conn, addr = server.accept()
    print("Connected to", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("Connection closed")
            break
        print(data)
        conn.sendall(data)
    conn.close()


if __name__ == "__main__":
    main()
