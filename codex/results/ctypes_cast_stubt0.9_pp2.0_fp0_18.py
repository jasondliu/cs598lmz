import ctypes
ctypes.cast(5, ctypes.py_object)
</code>
When I run the cell, I get the following error message:
<code>---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
&lt;ipython-input-44-b9abb4617d50&gt; in &lt;module&gt;()
----&gt; 1 ctypes.cast(5, ctypes.py_object)

TypeError: expected c_void_p, got int
</code>
The code works fine in a different machine (with the same OS and Python version). This problem started happening all of a sudden, so I suspect it's caused by some system update but I haven't found anything helpful by searching.
Thanks for any help!


A:

This was a bug in IPython that only affected the Linux version, it's been fixed in a PR here, and the fix is already in the latest IPython dev release.

