import threading
threading.Thread(target=app.run, kwargs={"host":"0.0.0.0","port":80}).start()
