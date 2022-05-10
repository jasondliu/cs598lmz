import sys, threading

def run():
    # Create the server, binding to localhost on port 9999
    server = ThreadedTCPServer(('localhost', 9999), ThreadedTCPRequestHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

def main():
    run()

if __name__ == "__main__":
    main()
