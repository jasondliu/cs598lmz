import threading
threading.Thread(target=run_server).start()

# Run the server's main loop
server.serve_forever()
