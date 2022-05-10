import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print("Signal handler called with signal", signum)
    else:
         print("Done.")

def main():
    for i in range(N):
        signal.signal(signal.SIGALRM, handler)
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print("Sleeping as ual.")
        time.sleep(1)
</code>
The prints are alternating and the time.sleep is not interrupted by the signal handler I presume. Why?
It can be seen that the handler is called every second after the first delay because it is not removed in the handler's code. 
The doc just says that "this clock continues to tick while the program is executing a signal handler".
I don't know if you can sleep in the signal handler. 

