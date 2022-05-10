import sys, threading

def run():
    port = 8080
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    print("Listening on port " + str(port) + "...")
    httpd = HTTPServer(('', port), RequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    threading.Timer(1.0, run).start()
    print("Loading the model...")
    load_model()
    print("Model ready!")
