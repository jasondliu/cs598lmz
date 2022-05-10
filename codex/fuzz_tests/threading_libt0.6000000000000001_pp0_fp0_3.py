import threading
threading.Thread(target=lambda: webbrowser.open_new("http://localhost:8000/")).start()

# Local server
httpd = socketserver.TCPServer(("", PORT), MyHandler)
httpd.serve_forever()
