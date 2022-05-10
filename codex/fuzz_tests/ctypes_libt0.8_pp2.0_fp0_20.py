import ctypes
ctypes.__file__
</code>
and
<code>import sys
sys.version
</code>
and then combine like
<code>ctypes.__file__ + "\n" + sys.version
</code>
This should give you the same result as running <code>python -vv</code>

