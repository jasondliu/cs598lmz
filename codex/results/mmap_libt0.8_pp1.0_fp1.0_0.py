import mmap
+
+def main():
+    input_file = sys.argv[1]
+
+    f = open(input_file, "r+")
+    # memory-map the file, size 0 means whole file
+    mm = mmap.mmap(f.fileno(), 0)
+    # read content via standard file methods
+    mm.readline()  # read an entire line
+    mm.seek(0)  # rewind
+    l = mm.readline()  # read an entire line
+    print(l)
+
+    print("Implement me!")
+
+if __name__ == "__main__":
+    main()

