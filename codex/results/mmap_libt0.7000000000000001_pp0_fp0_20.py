import mmap
+import sys
+
+
+def main():
+    print("Mmap file: " + sys.argv[1])
+    print("Start offset: " + sys.argv[2])
+    print("End offset: " + sys.argv[3])
+
+    f = open(sys.argv[1], "r+b")
+    # memory-map the file, size 0 means whole file
+    mm = mmap.mmap(f.fileno(), 0)
+    mm[int(sys.argv[2]):int(sys.argv[3])] = '\0'
+    mm.close()
+
+
+if __name__ == "__main__":
+    main()

