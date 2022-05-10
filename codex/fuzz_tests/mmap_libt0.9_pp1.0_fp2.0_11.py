import mmap
+import sys
+import csv
+import copy
+def main():
+    if len(sys.argv) != 4:
+        print("Enter valid number of argument")
+        return 0
+    else:
+        arr = [[] for j in range(11)]
+        filename = sys.argv[1]
+        k = sys.argv[2]
+        output = sys.argv[3]
+        #print (k)
+        
+        for j in range(len(sys.argv)-1):
+            f = open(sys.argv[j+1], 'r+')
+            mappedfile = mmap.mmap(f.fileno(), 0)
+            count = 1
+            while True:
+                line = mappedfile.readline()
+                if not line: break
+                if count != 2:
+                    arr[j].append(line)
+                    count += 1
+                    #print (arr[j][0])
+#                     if line[-1] == '\n': line =
