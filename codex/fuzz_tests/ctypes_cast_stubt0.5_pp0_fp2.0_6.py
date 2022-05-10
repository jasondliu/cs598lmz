import ctypes
ctypes.cast(0, ctypes.py_object)
# segfaults
</code>
I'm trying to get the top-level module object, so that I can call <code>getattr</code> on it.
<code>import sys
sys.modules[__name__]
# works

import ctypes
ctypes.cast(0, ctypes.py_object).value
# segfaults
</code>
I'm trying to get the top-level module object, so that I can call <code>getattr</code> on it.
<code>import sys
sys.modules[__name__]
# works

import ctypes
ctypes.cast(0, ctypes.py_object).value
# segfaults
</code>
I'm trying to get the top-level module object, so that I can call <code>getattr</code> on it.
<code>import sys
sys.modules[__name__]
# works

import ctypes
ctypes.cast(0, ctypes.py_object).value
# segfaults
</code>
I
