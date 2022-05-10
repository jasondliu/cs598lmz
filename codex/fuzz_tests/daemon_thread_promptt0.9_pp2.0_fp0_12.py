import threading
# Test threading daemon to re-launch tests every 2 secs
# When stopped, all threads get terminated
class Thread(threading.Thread):
    def __init__(self, app):
        self.app = app
        self.stored = []
        threading.Thread.__init__(self)
        self.daemon = True                            # so it can be terminated

    def run(self):
        while True:
            mutex.acquire()
            controllers = self.app.controller_store
            for c in controllers:
                for k in controllers[c]['term']:
                    self.stored.append((c, k))
            mutex.release()
            for c, k in self.stored:
                try:
                    m = hashlib.sha1()
                    m.update(str(controllers[c][k]))
                    self.app.controller_store[c]['hashes'][k] = m.hexdigest()
                except:
                    continue
            self.stored = []

class MainWindow(QtGui.QMainWindow, Ui_MainWindow
