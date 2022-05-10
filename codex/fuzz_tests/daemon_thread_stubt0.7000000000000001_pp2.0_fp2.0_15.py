import sys, threading

def run():
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer(("", PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def get_port():
    return PORT


# Thread
t = threading.Thread(target=run)
t.daemon = True
t.start()

# Main
if __name__ == "__main__":
    pass
