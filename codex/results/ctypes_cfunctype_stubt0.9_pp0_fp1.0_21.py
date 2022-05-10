import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1,2]
print fun()
</code>
This should print <code>[1,2]</code>, but instead it gives:
<code>Traceback (most recent call last):
  File "/home/david/temp/fun.py", line 13, in &lt;module&gt;
    print fun()
  File "/usr/lib/python2.7/lib-dynload/cPickle.so", line 665, in save_tuple
  File "/usr/lib/python2.7/lib-dynload/cPickle.so", line 637, in save
  File "/usr/lib/python2.7/lib-dynload/cPickle.so", line 665, in save_tuple
cPickle.PicklingError: Can't pickle &lt;type 'list'&gt;: attribute lookup __builtin__.list failed
</code>
What do I need to do to be able to pickle a list and return it without getting this error?


A:

<code>ctypes</code> by default uses the
