import threading
# Test threading daemon
#
#
import time
class MyThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self._running = True
        self._pause = True
        self._pause_cond = threading.Condition(threading.Lock())
    def pause(self):
        self._pause = True
        self._pause_cond.acquire()
    def resume(self):
        self._pause = False
        self._pause_cond.notify()
        self._pause_cond.release()
    def stop(self):
        self._running = False
    def run(self):
        while self._running:
            with self._pause_cond:
                while self._pause:
                    self._pause_cond.wait()
                print('do stuff')
                time.sleep(1)
</code>

