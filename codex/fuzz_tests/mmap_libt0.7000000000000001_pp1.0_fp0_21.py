import mmap
+import time
+import re
+
+# Initialize GPIO
+GPIO.setmode(GPIO.BOARD)
+GPIO.setup(12, GPIO.OUT)
+
+# Set Pin 12 to PWM with 50 Hz
+p = GPIO.PWM(12, 50)
+p.start(0)
+
+# Open the file in read mode and read it
+f = open("/dev/mem", "r")
+mem = mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_READ)
+
+# Keep track of the number of times the temperature has been read
+counter = 0
+
+while True:
+    # Increment the counter
+    counter += 1
+    # Read from the file
+    mem.seek(0)
+    # Regex to find the temperature
+    temp = re.findall("t=(.+)'C", mem.readline())
+    # If the temperature has been found
+    if temp:
+        # Convert the temperature to float
+        temp =
