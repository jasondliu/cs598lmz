import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.path =f'/data/2.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "Error File Not Found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

#configurar la conexión con el servidor
httpd = HTTPServer(('localhost', 8080), Handler) # se vincula el servidor con el hilo Handler
httpd.serve_forever()
