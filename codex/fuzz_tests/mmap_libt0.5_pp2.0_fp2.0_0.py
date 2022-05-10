import mmap
+import os
+import re
+import time
+
+# determine if application is a script file or frozen exe
+if getattr(sys, 'frozen', False):
+    application_path = os.path.dirname(sys.executable)
+elif __file__:
+    application_path = os.path.dirname(__file__)
+
+
+class MyText:
+
+    def __init__(self):
+        self.window = tk.Tk()
+        self.window.title("MyText")
+        self.window.geometry("800x600")
+        self.window.resizable(False, False)
+        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
+
+        self.notebook = ttk.Notebook(self.window)
+        self.notebook.pack(fill="both", expand="yes")
+
+        self.menu_bar = tk.Menu(self.window)
+        self.window.config(
