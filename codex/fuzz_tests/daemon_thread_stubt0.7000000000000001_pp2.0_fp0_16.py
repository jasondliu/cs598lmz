import sys, threading

def run():
    sys.stdout.write('hello\n')
    sys.stdout.flush()
    sys.stdout.write('world\n')
    sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()
</code>
The output contains one or the other, but not both.
With <code>python -u</code>:
<code>&gt; python -u test.py
hello
world
&gt; python -u test.py
hello
&gt; python -u test.py
world
</code>
Without <code>python -u</code>:
<code>&gt; python test.py
&gt; python test.py
hello
&gt; python test.py
world
</code>
I am running Python 2.7.3 on Cygwin.  Is this a known problem?  Is there a fix?


A:

That's because the Python's <code>stdout</code> is buffered by default. Use <code>-u</code> switch to turn off the buffering.

