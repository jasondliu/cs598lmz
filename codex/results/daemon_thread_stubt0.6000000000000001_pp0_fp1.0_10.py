import sys, threading

def run():
    x = input('Enter: ')
    print('You entered:', x)
    sys.exit()

t = threading.Thread(target=run)
t.start()

while True:
    time.sleep(0.001)
</code>
This code works fine in Python 3.5.2 (Windows), 3.6.1 (Windows) and 3.6.1 (Linux), but fails in Python 3.7.0 (Windows) and 3.7.0 (Linux):
<code>Enter: test
You entered: test
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python3.7/threading.py", line 917, in _bootstrap_inner
    self.run()
  File "test.py", line 9, in run
    x = input('Enter: ')
  File "&lt;string&gt;", line 1, in &lt;module&gt;
EOFError: EOF when reading a line

Process finished with exit code 0
</code>
Is this a bug, or
