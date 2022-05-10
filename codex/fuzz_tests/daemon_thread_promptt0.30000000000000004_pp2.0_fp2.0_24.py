import threading
# Test threading daemon
# https://stackoverflow.com/questions/19071512/run-infinite-loops-using-threads-in-python

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

class MyThread(StoppableThread):
    def run(self):
        while not self.stopped():
            print('working')
            time.sleep(1)

if __name__ == '__main__':
    t = MyThread()
    t.start()
    time.sleep(5)
    t.stop()
    t.join()

# Test threading event
# https://stack
