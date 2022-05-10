import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("done")

def main():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 1e-6)
    while delays:
        signal.pause()

if __name__ == '__main__':
    main()
</code>
I am only able to handle about 1000, give or take a few dozen, events per second. I know this is likely OS/Python implementation related, but how can I get around it?
I'm currently running this code on MacOSX 10.6, but an answer for Linux/BSD platforms would be appreciated too.


A:

One way to do this is to write the delays to a FIFO, and then start a child process that keeps reading from the FIFO and triggering the events.
Example:
<blockquote>
<p>import itertools, os<br/>
  import time, signal, random<br/>
  import glob, tempfile, os, subprocess  </p>
<p>def handler(signum=None,
