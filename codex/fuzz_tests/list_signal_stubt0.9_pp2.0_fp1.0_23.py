import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        return
    signal.setitimer(signal.ITIMER_REAL, 0)
    
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0) # Allow control-C
print("Starting sample period... ")
signal.setitimer(signal.ITIMER_REAL, 1)

print("Collecting samples... ")

while delays:
    continue
    
print("Sample period complete")
</code>

This is where I'm at right now. I stripped out some of the code to just include the bare minimum so I don't include unnecessary code and confuse anyone trying to help me.
With this solution, I can create a timer object, set the timeout to 10 ms and the interval to 10 ms. If I set up my while loop, every time it goes through the loop if it doesn't recieve a signal, which I have as 'enter pressed' , it will then cause the signal to go off and do the timeout function. This is obviously not a good solution because I now have to keep looping back
