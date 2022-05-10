import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [
        ('x', ctypes.c_int),
        ('passed', ctypes.c_bool)
    ]

if len(sys.argv) &gt; 1:
    t = multiprocessing.Process(target=f)
else:
    t = multiprocessing.Process(target=f, args=(S(),))

t.start()
t.join()
</code>
Which provides the same behavior:
<code>gccrand@hawking:~/tmp$ python a.py
Let's use the struct!
Exception in thread Thread-1 (most likely raised during interpreter shutdown):
Traceback (most recent call last):
  File "/home/gccrand/tmp/a.py", line 13, in f
    print(s.passed)
AttributeError: 'S' object has no attribute 'passed'
Exception in thread Thread-2 (most likely raised during interpreter shutdown):
Traceback (most recent call last):
  File "/home/gccrand/tmp/a.py", line 13
