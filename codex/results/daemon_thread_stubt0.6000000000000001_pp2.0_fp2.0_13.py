import sys, threading

def run():
    for i in range(5):
        print("I am thread %d" % i)

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    t.join()
</code>
This code runs perfectly fine.
However, if I change the <code>target</code> parameter to <code>run()</code> (without the parentheses), then it doesn't work.
<code>import threading

def run():
    for i in range(5):
        print("I am thread %d" % i)

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    t.join()
</code>
This gives me the following error:
<code>Exception in thread Thread-1:
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()

