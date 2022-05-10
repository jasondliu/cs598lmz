import gc, weakref
+
+__all__ = ['AAPI']
+
+class BaseAPI(object):
+    def __init__(self):
+        self._token = None
+        self.func_cache = weakref.WeakValueDictionary()
+
+    @property
+    def token(self):
+        return self._token
+
+    @token.setter
+    def token(self, v):
+        self._token = v
+
+    def _get_url(self, url, method='GET'):
+        if self.token:
+            headers = {'Authorization': 'Bearer %s' % self.token}
+        else:
+            headers = {}
+        resp = requests.request(method, url, headers=headers)
+        if resp.status_code >= 300:
+            raise Exception('%s returned status code %s' % (url, resp.status_code))
+        return resp.json()
+
+    def __getattr__(self, name):
+        try:
+            return self.func
