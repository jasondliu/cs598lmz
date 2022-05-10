import mmap
+import glob
+import datetime
+import sys
+import time
+
+
+date_format = '%Y-%m-%d %H:%M:%S '
+update_rate = 60
+
+driver = 'cdm'
+try:
+    driver = sys.argv[1]
+except:
+    pass
+pattern = '/var/log/pmdsolr*/solr%s.log' % driver
+files = glob.glob(pattern)
+
+def readline(mmapobj):
+    idx = mmapobj.find('!');
+    while idx != -1:
+        return mmapobj[0:idx];
+    return "";
+
+def get_whole_line(mmapobj):
+    idxend = mmapobj.find('\n');
+    
+
+def readlog(file):
+    f = open(file, 'r+b');
+    mm = mmap.mmap(f.fileno(), 0, access=mm
