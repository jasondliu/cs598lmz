import select
+import sys
+import termios
+import tty
+
+def getchar():
+    fd = sys.stdin.fileno()
+    old_settings = termios.tcgetattr(fd)
+    try:
+        tty.setraw(sys.stdin.fileno())
+        ch = sys.stdin.read(1)
+    finally:
+        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
+    return ch
+
+def main():
+    '''
+    Ctrl-C will cleanly exit the example
+    '''
+    # Instantiate CIM-Java
+    cim = jnius_config.class_path_show_warning(False)
+    cim = jnius.autoclass('org.sleuthkit.datamodel.CIMJava')
+    data_source = cim.createDataSource(sys.argv[1])
+    # Create the Sleuth Kit case
+    skCase = cim.createCase("
