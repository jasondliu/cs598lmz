import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def process(signum=None, frame=None):
    print("Processing frame %s" % frame)
    handler()

def main():
    signal.signal(signal.SIGALRM, process)
    handler()
    signal.pause()

if __name__ == "__main__":
    main()
</code>
The above runs fine on my machine:
<code>$ time python test.py 
Processing frame &lt;frame object at 0x10c81e4d0&gt;
Processing frame &lt;frame object at 0x10c81e4d0&gt;
Processing frame &lt;frame object at 0x10c81e4d0&gt;
Processing frame &lt;frame object at 0x10c81e4d0&gt;
Processing frame &lt;frame object at 0x10c81e4d0&gt;
Processing frame &lt;frame object at 0x10c81e4d0&gt;
Processing frame &lt;frame object at 0x10c81e4d0&
