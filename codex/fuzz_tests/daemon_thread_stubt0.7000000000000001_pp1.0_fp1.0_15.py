import sys, threading

def run():
    for i in range(3):
        print("thread {}".format(i))

threads = [threading.Thread(target=run) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()
</code>
In Python 3.7, however, only the first thread is run, and the other two are not.
<code>thread 0
</code>
In this case, the output is printed to <code>stdout</code>, so the issue is likely related to file descriptors.
I have tried the same example in Python 3.6, and the code works as expected.
Is this an expected behavior?


A:

The problem is that Python (or at least Python 3.7) has a race condition in <code>Py_Finalize()</code> which causes it to incorrectly close stdout. You can see this with the following Python program:
<code>import sys, threading

def run():
    for i in range(3):
        print("thread {}".format(i))

threads = [threading.Thread(target
