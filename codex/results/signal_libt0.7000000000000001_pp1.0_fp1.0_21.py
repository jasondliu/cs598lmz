import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL)  # KeyboardInterrupt: Ctrl-C


def stop_handler(sig, frame):
    print("Ctrl+Z pressed")
    sys.exit(0)


def handle_connection(connection, address):
    try:
        full_data = b""
        while True:
            data = connection.recv(1024)
            if not data:
                print("no data")
                break
            full_data += data
            print("full_data = {}".format(full_data))
    finally:
        connection.close()


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", port))
    sock.
