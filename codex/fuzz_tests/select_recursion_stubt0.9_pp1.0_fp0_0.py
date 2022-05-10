import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    for i in xrange(1000):
        a.append(F())
        b = select.select([], [], a, 0.01)
    print "loop done"

thread.start_new_thread(test_select_mutated, ())

def test_callback():
    def foo():
        print "called"
    import carbon
    carbon.AppleEvents.AEInstallEventHandler(0, 0, foo)

import threading
import time
class Daemon(threading.Thread):
    def start_and_wait(self):
        self.start()
        while not getattr(self, 'done', False):
            time.sleep(1)

class EventLoop(Daemon):
    def run(self):
        import Carbon.Cm

        e1 = c.CreateEvent(0, 0, 0, 'event')
        c.WaitNextEvent(0, e1)
        self.done = True

class PortLoop(Daemon):
    def run(self):
        import Carbon.Cm
        p1 = c.CreatePort
