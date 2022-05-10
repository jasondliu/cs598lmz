import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
handler()

class MyThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self._running = True
        self.daemon = True

    def run(self):
        while self._running:
            time.sleep(1)

    def stop(self):
        self._running = False

t = MyThread()
t.start()

time.sleep(3)
print 'exiting'
t.stop()
</code>
The above code prints:
<code>exiting
Traceback (most recent call last):
  File "timer_thread.py", line 28, in &lt;module&gt;
    time.sleep(3)
  File "/usr/lib/python2.6/
