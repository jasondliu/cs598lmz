import mmap
+import re
+import os
+
+def write_to_file(file1,text1):
+    with open(file1, "a") as myfile:
+        myfile.write(text1)
+
+folder = "/home/hetal/Python_practice_examples/writefile_examples/documents/"
+file = 'unclosed.txt'
+with open(folder+file, 'r') as f:
+    data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+    if data.find('}') == -1:
+        print ('file not closed')
+        branch_name = re.search('{branch:.*}',data)
+        if branch_name:
+            print (branch_name.group(0))
+            text = str(branch_name.group(0)).replace('{branch:','')
+            print (text[:-1])
+        else:
+            print ("not found")
+            txt = """
+
