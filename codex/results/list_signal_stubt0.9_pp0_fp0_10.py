import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit()

print('Setting up signal handling')
signal.signal(signal.SIGALRM, handler)

handler()
print('Starting')

while True:
    signal.pause()

</code>
This approach was taken from here: http://www.evanjones.ca/python-timer-example.html. However, here the function 'handler' is called within the file. When it comes to (1) calling 'handler', inside the file or at the terminal, I keep getting:
<code>File "test_timer.py", line 18, in &lt;module&gt;
    handler()
TypeError: handler() takes from 0 to 2 positional arguments but 3 were given
</code>
What am I missing?


A:

When you execute:
<code>handler()
</code>
you actually call <code>handler</code> with 3 arguments -- two passed by Python as <code>None</code> and <code>&lt;frame object at 0x7fe1cc6bdc18&gt;</code>, and the third
