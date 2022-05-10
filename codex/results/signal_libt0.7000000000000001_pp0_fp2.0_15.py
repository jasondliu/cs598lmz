import signal
signal.signal(signal.SIGINT, handler)

def main():
    """The main function."""
    try:
        main_loop()
    except KeyboardInterrupt:
        print("Bye")
        sys.exit(0)

def main_loop():
    """The main loop."""
    # start the server, listen to new clients and handle all the requests
    with start_server(('', PORT)) as server:
        while run:
            try:
                client = server.accept_client()
                client.send("Welcome to the chatroom!".encode('utf-8'))
                client.send("What is your name?".encode('utf-8'))
                name = client.recv(1024)
                name = name.decode('utf-8')
                client.send("Welcome to the chatroom, {}!".format(name).encode('utf-8'))
                client.send("Please enter your message:".encode('utf-8'))
                # start a new thread
                thread = threading.Thread(target=handle_client, args
