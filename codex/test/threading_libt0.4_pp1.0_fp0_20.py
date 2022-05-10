import threading
threading.stack_size(67108864) # 64MB stack

# Create a class to handle HTTP requests from the client.
class HTTPRequestHandler(BaseHTTPRequestHandler):
    # Handle a GET request from a client.
    def do_GET(self):
        # Get the path of the request.
        path = self.path

        # Check if the request is for the root path.
        if path == '/':
            # Set the response code.
            self.send_response(200)

            # Set the response headers.
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Send the response.
            self.wfile.write(b'<html><body>Hello, world!</body></html>')
        else:
            # Set the response code.
            self.send_response(404)

            # Set the response headers.
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Send the response.
