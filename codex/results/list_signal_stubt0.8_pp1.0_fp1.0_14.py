import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

if os.name == 'posix':
    # Exit when the last timer fires
    signal.signal(signal.SIGALRM, handler)
    # Set first timer
    handler()

else:
    # Windows
    import threading
    class Timer(threading.Thread):
        def run(self):
            while True:
                handler()
                time.sleep(0)
    Timer().start()

# Process events
import Tkinter
root = Tkinter.Tk()
root.mainloop()
</code>

