import mmap
+import random
+import argparse
+
+
+parser = argparse.ArgumentParser()
+parser.add_argument('-f', '--file', help='filepath to file we are reading from')
+parser.add_argument('-s', '--size', help='number of bytes to read')
+parser.add_argument('-o', '--output', help='filepath to write output to (default to STDOUT)')
+
+args = parser.parse_args()
+
+
+def main():
+    if args.file:
+        if args.output:
+            out = open(args.output, 'w')
+        else:
+            out = sys.stdout
+
+        with open(args.file, 'r') as f:
+            size = f.seek(0, 2)
+            buf = mmap.mmap(f.fileno(), 0)
+            random_pos = random.randint(0, size - int(args.size))
+            out.write(buf[random_pos:random_pos
