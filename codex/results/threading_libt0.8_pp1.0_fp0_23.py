import threading
threading.Thread(target=app.run, kwargs={'host': 'localhost', 'port': 5000, 'debug': True}).start()
