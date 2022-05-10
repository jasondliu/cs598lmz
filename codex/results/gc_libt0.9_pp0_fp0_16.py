import gc, weakref
+
+from twisted.internet.defer import DeferredLock, Deferred, maybeDeferred
+from twisted.python.failure import Failure
+
+
+class Deferredme(object):
+    """A class for handling deferreds.
+
+    Deferredme class is one of the main parts of the transaction
+    system.  It listens for events in a CallLater container, and when
+    an event is fired, it calls a deferred.  If a deferred fails when
+    it is fired, it will be re-registered if there is enough time
+    left.  Otherwise, the error is given to the consumer object.
+    """
+
+    def __init__(self, consumer=None, executionTime=None):
+        """Set up this deferredme.
+
+        consumer -- a consumer object, used for raising errors when
+                    the Time's up.
+        executionTime -- a tuple with two integers, describing the
+                         deadline for execution.
+        """
+        self._consumer = consumer
+        self._executionTime = executionTime
+        self._
