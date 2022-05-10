import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

s = S()
s.a = 2
s.b = 3
s.c = 4
s.d = 5
print s.x
</code>
Try it online!
This would print <code>1</code>. Whether you get that or a crash or raise an exception or get <code>0</code> will depend on your particular build of Python. If you're running Python 3.4, for example, you'll get a crash; for example, on my computer:
<code>Fatal Python error: init_sys_streams: can't initialize sys standard streams
Traceback (most recent call last):
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site.py", line 548, in &lt;module&gt;
    main()
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site.py", line 530, in main
    known_paths = addusersitepackages(known_paths
