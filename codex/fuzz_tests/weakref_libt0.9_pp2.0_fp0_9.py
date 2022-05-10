import weakref
+import threading
+import optparse
+
+class kk_OptParse(optparse.OptionParser):
+    def error(self, msg):
+        print msg
+        self.print_help()
+        sys.exit(1)
+
+class VutScanner:
+    def __init__(self, options, vut_files):
+        self.vut_files = vut_files
+        self.vut_file_dict = {}
+        self.vut_details = {}
+        self.options = options
+
+    def __add_parser(self, filename, vut_file):
+        dom = xml.dom.minidom.parse(vut_file)
+        path = dom.getElementsByTagName("path")[0]
+        target_path = path.getAttribute("target")
+        if self.options.target not in target_path:
+            return
+        if self.options.scanner == None:
+            self.options.scanner = "."
+            for
