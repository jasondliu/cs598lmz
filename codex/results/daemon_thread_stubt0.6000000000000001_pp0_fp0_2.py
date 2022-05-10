import sys, threading

def run():
    server = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), server)
    print "serving at port", PORT
    httpd.serve_forever()

# Start the web server in a new thread
threading.Thread(target=run).start()

# Open the browser in a new thread
threading.Thread(target=webbrowser.open, args=('http://localhost:%s/index.html' % PORT,)).start()

# Wait for user input
raw_input('Press Enter to exit...')
</code>

