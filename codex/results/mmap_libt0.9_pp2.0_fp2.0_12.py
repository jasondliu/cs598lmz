import mmap
+
+def parse(line):
+	parts = line.split("|")
+
+	if len(parts) == 2:
+		(key, value) = parts
+		print "{0}\t{1}".format(key, value)
+
+
+f = open(argv[1], "r+b")
+buf = mmap.mmap(f.fileno(), 0)
+line = buf.readline()
+
+while line:
+	parse(line)
+	line = buf.readline()
+
+buf.close()
+f.close()
+

