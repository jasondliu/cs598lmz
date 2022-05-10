import sys, threading

def run():
    while True:
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)

t = threading.Thread(target=run)
t.daemon = True
t.start()

time.sleep(5)
</code>
I would expect it to print out a line of dots and then exit without any error. But instead it doesn't print anything until it exits and then prints out the dots all at once and it ends with an error:
<code>$ python test.py
..........Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    time.sleep(5)
  File "/usr/lib/python2.7/threading.py", line 801, in __bootstrap_inner
    self.run()
  File "/usr/lib/python2.7/threading.py", line 754, in run
    self.__target(*self.__args, **self.__kwargs)
  File "test.py", line 5, in run
    sys.
