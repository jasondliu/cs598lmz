import sys, threading

def run():
    print("Updating")
    #while True:
        #pass

def main():
    try:
        server = ThreadedTCPServer(("127.0.0.1", 2017), ThreadedTCPRequestHandler)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)
        while True:
            pass
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
