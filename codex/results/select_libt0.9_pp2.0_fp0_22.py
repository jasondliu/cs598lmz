import select
+    need_sparse_mapping = False
+except ImportError:   # Windows
+    from select32 import select  # pylint:disable=import-error
+    need_sparse_mapping = True
+
+import itertools
+import six
+
+
+class SocketServer(object):
+    """
+    A simple synchronous event-driven I/O implementation on top of sockets
+    The server is designed to be single threaded.
+    """
+
+    def __init__(self):
+        self._map = {} if need_sparse_mapping else {}
+
+        self._listeners = {}
+        self._wallets = {}
+        self._peer_to_wallet_map = {}
+        self._peers = set()
+
+    def listen(self, socket):
+        self._listeners[socket] = []
+        self._map[socket] = self._listeners
+
+    def add(self, socket):
+        assert socket not in self._wallets
+        self._wal
