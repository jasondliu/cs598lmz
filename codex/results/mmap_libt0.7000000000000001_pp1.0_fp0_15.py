import mmap
+import re
+import sys
+import time
+
+# i2c address
+address = 0x69
+
+def read_word(addr):
+    high = bus.read_byte_data(address, addr)
+    low = bus.read_byte_data(address, addr+1)
+    val = (high << 8) + low
+    return val
+
+def read_word_2c(addr):
+    val = read_word(addr)
+    if (val >= 0x8000):
+        return -((65535 - val) + 1)
+    else:
+        return val
+
+def dist(a,b):
+    return math.sqrt((a*a)+(b*b))
+
+def get_y_rotation(x,y,z):
+    radians = math.atan2(x, dist(y,z))
+    return -math.degrees(radians)
+
+def get_x_rotation(x,y,z):
+    radians =
