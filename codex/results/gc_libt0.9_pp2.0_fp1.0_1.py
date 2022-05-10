import gc, weakref, os, glob
+from matplotlib.testing.noseclasses import ImageComparisonFailure
+from matplotlib.testing.compare import compare_images
+from matplotlib import cbook
+from matplotlib import pyplot as plt
+from matplotlib import style
+
+image_directories = [join(rcParams['datapath'], 'images')]
+
+def setup():
+    style.use('default')
+    _disable_file_cache()
+    plt.close('all')
+
+# disable the default file caching for faster tests running
+def _disable_file_cache():
+    class NullFileCache(object):
+        def __init__(self): pass
+        def __call__(self):
+            return self
+        def __enter__(self): pass
+        def __exit__(self, *args): pass
+        def cache(self, *args, **kwargs): pass
+        def read_cached(self, *args, **kwargs): pass
+        def write_cached(
