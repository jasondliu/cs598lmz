import threading
threading.stack_size(32768)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print("Server starting...")
    while True:
        client, address = server.accept()
        client.settimeout(60)
        threading.Thread(target = handle_client,args = (client,address)).start()

def handle_client(client, address):
    size = 1024
    while True:
        try:
            data = client.recv(size)
            if data:
                # Set the response to echo back the recieved data
                response = data
                client.send(response.encode("utf-8"))
            else:
                raise error("Client disconnected")
        except:
            client.close()
            return False

if __name__ == "__main__":
    main()
