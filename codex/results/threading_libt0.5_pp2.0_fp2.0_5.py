import threading
threading.Thread(target=server.serve_forever).start()

while 1:
    time.sleep(1)
