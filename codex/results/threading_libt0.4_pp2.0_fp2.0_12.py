import threading
threading.Thread(target=lambda: None).start()

# Start the server
server.serve_forever()
