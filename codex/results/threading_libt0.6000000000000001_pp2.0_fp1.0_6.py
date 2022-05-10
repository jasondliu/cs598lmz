import threading
threading.stack_size(1024*1024*1024)

def main():
    print("Starting server...")
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ', PORT_NUMBER)
    print("Server Ready")
    # Wait forever for incoming htto requests
    server.serve_forever()

if __name__ == '__main__':
    main()
