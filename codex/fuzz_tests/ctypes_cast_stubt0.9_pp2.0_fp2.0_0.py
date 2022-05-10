import ctypes
ctypes.cast("Abc", ctypes.py_object)
ctypes.cast(()); # Doesn't crash
ctypes.cast((), ctypes.py_object)
</code>
In 3.2, however, I get
<code>Traceback (most recent call last):
  File "a.py", line 4, in &lt;module&gt;
    ctypes.cast((), ctypes.py_object)
TypeError: a bytes-like object is required, not 'tuple'
</code>
for the last line.
I am using Python 3.2.3, but doesn't seem to make a difference.
Why is there a difference?
More generally, what is the correct behavior, and why?
NOTE: This is fixed in Python 3.3 (thanks to Ned Batchelder for pointing that out).
ANSWER: Stefan Krah said that I should file a bug report. I guess this is the responsibility of whoever changed it in the first place.


A:

It does seem to be a bug that it's not consistent, between python3.2 and python3.3, between the default and the <code>
