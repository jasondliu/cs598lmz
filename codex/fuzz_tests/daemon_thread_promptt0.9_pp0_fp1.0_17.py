import threading
# Test threading daemon
registry = []
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.writelock = threading.Lock()
        path = self.path
        # This can only GET
        if path == '/heartbeat':
            self.respond_ok()
        elif path == '/ip':
            self.respond_with_ips()
        elif path.startswith('/admin/'):
            self.serve_admin()
        elif path.startswith('/spark/'):
            self.serve_spark()
        else:
            self.respond_with_404()

        print(registry)

    def build_response(self, response, status=200):
        self.send_response(status)
        if self.path.endswith('json'):
            self.send_header('Content-type', 'application/json')
        else:
            self.send_header('Content-type', 'text/html')
        # Server should be able to serve this file
        self.end_headers()

        self
