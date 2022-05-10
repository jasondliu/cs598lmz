import sys, threading

def run():
    while True:
        print("thread running")
        time.sleep(1)

if __name__ == "__main__":
    print("main thread")
    thread = threading.Thread(target=run)
    thread.start()
    time.sleep(5)
    thread.stop()
</code>
However, running this code gives the following error:
<code>main thread
thread running
thread running
thread running
thread running
thread running
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python3.3/threading.py", line 639, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.3/threading.py", line 596, in run
    self._target(*self._args, **self._kwargs)
  File "test.py", line 8, in run
    time.sleep(1)
  File "/usr/lib/python3.3/threading.py", line 784, in stop
    raise RuntimeError('cannot stop thread which
