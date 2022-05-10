import sys, threading

def run():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    print("Running on port " + str(port))
    BaseHTTPServer.HTTPServer(("", port), MyHandler).serve_forever()

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
        time.sleep(1)
        self.send_response(200)
        self.end_headers()
        message = threading.currentThread().getName()
        self.wfile.write(message)
        self.wfile.write('\n')
        return

run()
