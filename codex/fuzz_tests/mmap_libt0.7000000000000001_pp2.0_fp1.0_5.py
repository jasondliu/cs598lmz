import mmap
+
+def find_Nth(haystack, needle, N):
+    start = haystack.find(needle)
+    while start >= 0 and N > 1:
+        start = haystack.find(needle, start+len(needle))
+        N -= 1
+    return start
+
+def find_last(s, t):
+    last_pos = -1
+    while True:
+        pos = s.find(t, last_pos+1)
+        if pos == -1:
+            return last_pos
+        last_pos = pos
+
+if __name__ == "__main__":
+    filename="/home/francois/Desktop/grep-test-files/files/100000000-lines-4.txt"
+    f = open(filename,'r')
+    s = mmap.mmap(f.fileno(),0,prot=mmap.PROT_READ)
+    print find_Nth(s,"\n",1000000)
+    print len(s)
+
