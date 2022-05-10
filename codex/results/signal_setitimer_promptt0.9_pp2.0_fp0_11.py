import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Time\'s up! Catch..'
    raise AlarmException

def test_setitimer():
    signal.signal(signal.SIGALRM, handler)
    setitimer(signal.ITIMER_REAL, 1, 0)

    try:
        while 1:
            time.sleep(0.2)
    except AlarmException:
        pass

if __name__ == '__main__':
    test_setitimer()
</code>
traceback:
<code>lab@lab-ws:~/Desktop/code/lab$ python test.py 
Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    setitimer(signal.ITIMER_REAL, 1, 0)
NameError: name 'setitimer' is not defined
</code>
How to correct the error?



A:

The documentation says <code>ITIMER_REAL</code> should be used for this.
