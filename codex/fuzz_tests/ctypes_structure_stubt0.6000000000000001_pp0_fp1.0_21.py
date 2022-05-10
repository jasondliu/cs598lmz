import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

print S.x.offset
print S.y.offset
</code>
outputs
<code>0
4
</code>
If I run the same code in Pycharm, I get
<code>Traceback (most recent call last):
  File "/home/user/PycharmProjects/test/test.py", line 7, in &lt;module&gt;
    print S.x.offset
AttributeError: 'member_descriptor' object has no attribute 'offset'
</code>
Does anyone know why this is happening? As far as I can tell, I am running the same version of Python on both IDLE and Pycharm.

