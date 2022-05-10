import mmap
+import os
+import sys
+
+def get_bar(F):
+
+	# barcode file
+	fc = open(F, "r")
+	line = fc.readline()
+	bar = ""
+
+	while line:
+		if line[0:1] == ">":
+			print("%s" % (bar))
+			bar = line.replace("\n", "")
+		else:
+			bar += line.replace("\n", "")
+
+		line = fc.readline()
+
+	fc.close()
+
+def find_barcode(F, barcode):
+	with open(F, "rb", 0) as file, \
+		mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
+		if s.find(barcode) != -1:
+			print("file: %s barcode: %s" % (F
