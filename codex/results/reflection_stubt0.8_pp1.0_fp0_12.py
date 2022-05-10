fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
if __debug__:
    # this should result in an exception
    fn()
    print("should not get here")
else:
    print("should expect an exception")
</code>
The output is:
<code>Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\python\debug_on.py", line 16, in &lt;module&gt;
    fn()
  File "C:\Users\Administrator\Desktop\python\debug_on.py", line 12, in &lt;lambda&gt;
    fn = lambda: None
  File "C:\Users\Administrator\Desktop\python\debug_on.py", line 9, in fn
    gi = (i for i in ())
TypeError: 'code' object is not iterable
</code>

