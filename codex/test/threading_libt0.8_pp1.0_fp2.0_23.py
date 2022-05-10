import threading
threading.Thread(target=app.run, kwargs={"debug": True}).start()
