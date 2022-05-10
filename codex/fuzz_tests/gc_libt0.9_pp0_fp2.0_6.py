import gc, weakref
+from . callbacks import *

+class Proto(object):
+    "delegate all members access to another instance"
+    def __init__(self, obj): self.obj = obj
+    def __getattr__(self,k): return getattr(self.obj,k)
+
+class Callback(object):
+    '''`Callback` can be used to schedule callbacks.  Function `f` will be called at
+    `interval` time with `args` and `kwargs`.  It is guaranteed that `f` will be called
+    at least once with `args` and `kwargs` or upon exception if `wait` is True.
+
+    **Examples**
+
+    The following example schedules a callback at 1 second interval.  When `Callback`
+    is garbage collected the timer is stopped automatically.
+
+        >>> import time, requests
+        >>> def f(x): print('url={}'.format(x)); requests.get(x).content; print('Done with {}'.format(x))
+        >>> x = Callback(f,
