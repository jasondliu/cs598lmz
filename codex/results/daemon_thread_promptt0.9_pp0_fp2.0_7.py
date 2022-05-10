import threading
# Test threading daemon

class DaemonThread(threading.Thread):
    def __init__(self):
        self.stop_event = threading.Event()
        threading.Thread.__init__(self)

    def stop(self):
        self.stop_event.set()

    def run(self):
        while not self.stop_event.is_set():
            print ("running")
            time.sleep(1)


daemon = DaemonThread()
daemon.start()
while True:
    print ("Command: ")
    if input() == "q":
        daemon.stop()
        break
