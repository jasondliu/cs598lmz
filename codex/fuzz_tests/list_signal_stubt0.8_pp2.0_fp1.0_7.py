import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    signal.pause()

print('Done after {} iterations'.format(N))
 
</code>
The above code runs on Ubuntu 18.04. How could it be ported to Windows?


A:

When you make a program that does work and waits for a signal to do more work then you have to make a loop. The loop can be an infinite loop, a loop with a fixed amount of iterations or it can be a loop where the number of iterations are determined by an outside event.
The only way to be able to have such a loop is to have the loop's run time be managed by the OS. That is, the loop must be willing to suspend itself and allow the OS to do other things.
To do this the loop must, at the end of each iteration, pause the execution of the loop. This is done by calling a function, usually named <code>sleep</code> or <code>pause</code>.
The <code>sleep</code> or <code>pause</code> function has to be a system call and not just
