import gc, weakref
+from collections import defaultdict
+from functools import partial
+from pprint import pprint
+
+class Object(object):
+    def __init__(self, name):
+        self.name = name
+
+    def __repr__(self):
+        return '<%s>' % self.name
+
+def ref_callback(obj, reference):
+    print 'Object %s was deleted!' % obj
+
+def weak_ref_callback(obj, reference):
+    print 'Object %s was deleted!' % obj
+
+def dump(obj):
+    print '\nObject: %s' % obj
+    print '    References: ', sys.getrefcount(obj)
+    print '    Reference Types: ', defaultdict(int, [(type(o), o) for o in gc.get_referrers(obj)])
+
+if __name__ == '__main__':
+    print 'Creating objects...'
+    obj1 = Object('Object 1')
+    obj2 = Object('Object 2')
