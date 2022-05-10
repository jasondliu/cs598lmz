import socketserver

HOST = ''
PORT = 80

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer((HOST, PORT), Handler)
httpd.serve_forever()
