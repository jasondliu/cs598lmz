import signal
signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        print 'You pressed Ctrl+C!'
        time.sleep(1)
except:
    print 'goodbye'
</code>


A:

You can use <code>signal.pause()</code>, but it only works in the main thread.  It will allow Python to process the signal and then return, but it won't interrupt the code you are running.  For example:
<code>import signal, time

def signal_handler(signal, frame):
    print 'got signal: %s at %s' % (signal, time.time())


signal.signal(signal.SIGINT, signal_handler)
print 'start'
signal.pause()
print 'end'
</code>
Doing a ^C at the terminal will print:
<code>start
got signal: 2 at 1417554341.73
</code>
and then return to the prompt.
So, if you want to interrupt some long-running code you have to add checking the signal
