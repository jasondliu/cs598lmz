import sys, threading

def run():
    while True:
        x = raw_input('input: ')
        print x

threading.Thread(target=run).start()
</code>
It works fine on Windows but on Ubuntu it outputs:
<code>input: a
Traceback (most recent call last):
   File "threading.py", line 6, in run
   File "threading.py", line 11, in &lt;module&gt;
threading.Thread(target=run).start()
</code>
I also tried using <code>thread.start_new_thread</code> but again, it works on Windows but is broken on Ubuntu.
How can I fix this?


A:

This is a known problem with Python threads on Linux.  There is a workaround:
<code>import sys, threading

def run():
    while True:
        x = raw_input('input: ')
        print x

def target():
    run()

t = threading.Thread(target=target)
t.daemon = True  # make interrupting the program with ctrl-C easier

