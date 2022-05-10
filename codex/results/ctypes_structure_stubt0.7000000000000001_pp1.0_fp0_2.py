import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
</code>
Then I create an instance of this class
<code>s = S()
s.x = 1
s.y = 2
s.z = 3
</code>
And then I want to put this structure in the heap
<code>s_addr = ctypes.c_int.from_address(id(s))
</code>
But when I try to access the member variables of <code>s</code> using <code>s_addr</code> like this:
<code>print s_addr.contents.x
</code>
I get the following message
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/ctypes/__init__.py", line 352, in __getattr__
    func = self.__getitem__(name)
  File "/usr/lib/python2.7/
