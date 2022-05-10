import gc, weakref
+
+TESSDATA_PREFIX = 'D:/tesseract/Tesseract-OCR_4.0.0/tessdata'
+
+get_ipython().system_raw('tesseract.exe --version')
+
+def cleanup_tess_proc():
+    while tesseract_proc and tesseract_proc.poll() is None:
+        tesseract_proc.terminate()
+atexit.register(cleanup_tess_proc)
+
+tesseract_proc = subprocess.Popen(['tesseract.exe'],
+  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
+atexit.register(tesseract_proc.terminate)
+
+def get_tess_stdin():
+    return tesseract_proc.stdin
+
+def get_tess_stdout():
+    return tesseract_proc.stdout
+

