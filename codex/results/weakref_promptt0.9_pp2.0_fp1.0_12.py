import weakref
# Test weakref.refwatcher API

thread_death = False

class Thread(object):
    die = False
    cv = threading.Condition()
    def f(self):
        # This thread will be doing stuff, but we want to make sure
        # that the main thread knows we are still alive.
        with self.cv:
            while not self.die:
                self.cv.wait(timeout=1.0)
        thread_death = True
    def __init__(self):
        self.t = threading.Thread(target=self.f)
        self.t.start()
    def __del__(self):
        with self.cv:
            self.die = True
            self.cv.notify()
        self.t.join()


def callback(arg):
    arg = "a" + "r" + "g"

def test_simple():
    with weakref.refwatcher(callback) as watcher:
        assert not watcher.dead
        t = Thread()
        with watcher.wait():
            pass
        wr = weakref.
