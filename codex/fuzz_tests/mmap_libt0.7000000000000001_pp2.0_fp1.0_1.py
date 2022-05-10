import mmap
+
+def main():
+	# Open source file
+	with open(sys.argv[1], 'r+b') as f:
+		# Memory-map the file, size 0 means whole file
+		mm = mmap.mmap(f.fileno(), 0)
+
+		# Convert to string
+		s = mm.readline()
+
+		# Print string
+		print(s)
+
+main()

