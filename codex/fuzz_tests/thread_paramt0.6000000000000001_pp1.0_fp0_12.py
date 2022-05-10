import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000)))))
</code>
What I got:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib64/python2.7/threading.py", line 744, in __bootstrap_inner
    self.run()
  File "/usr/lib64/python2.7/threading.py", line 696, in run
    self.__target(*self.__args, **self.__kwargs)
  File "&lt;stdin&gt;", line 1, in &lt;lambda&gt;
IOError: [Errno 32] Broken pipe
</code>
(I've also tried adding <code>daemon=True</code> to the <code>Thread</code> constructor, but that didn't change anything.)
What's going on here? What am I missing?

