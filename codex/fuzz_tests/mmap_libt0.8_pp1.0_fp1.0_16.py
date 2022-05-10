import mmap
+import tempfile
+
+try:
+    from msvcrt import getch  # try to import Windows version
+except ImportError:
+    def getch():   # define non-Windows version
+        import sys, tty, termios
+        fd = sys.stdin.fileno()
+        old_settings = termios.tcgetattr(fd)
+        try:
+            tty.setraw(sys.stdin.fileno())
+            ch = sys.stdin.read(1)
+        finally:
+            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
+        return ch
+
+
+class GameOfLife:
+    def __init__(self, rows, columns, padding=1):
+        self._rows = rows
+        self._columns = columns
+        self._padding = padding
+        self._live_cells = []
+        self._live_cell_count = 0
+
+    def set_live_cell(self, row, column):

