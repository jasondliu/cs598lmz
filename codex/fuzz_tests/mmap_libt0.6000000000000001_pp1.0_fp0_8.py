import mmap
+import os
+import re
+import shutil
+import subprocess
+import sys
+import tempfile
+import uuid
+
+
+# TODO: add support for more file types
+# TODO: add support for multiple files
+# TODO: add support for multiple pages
+
+
+def main():
+    supported_extensions = ['.pdf', '.png']
+    if len(sys.argv) != 2 or not sys.argv[1].lower().endswith(supported_extensions):
+        print('Usage: {} <file>'.format(sys.argv[0]))
+        print('Supported extensions: {}'.format(', '.join(supported_extensions)))
+        sys.exit(1)
+
+    image = sys.argv[1]
+    if not os.path.isfile(image):
+        print('File not found: {}'.format(image))
+        sys.exit(1)
+
+    if image.lower().endswith('.pdf'):
+        convert_pdf
