import mmap
+import csv
+import pdb
+import random
+
+trans_table= str.maketrans(' ',' ',string.punctuation)
+
+def write_json(json_file, word_dictionary):
+    
+    with open(json_file, 'w') as fp:
+        json.dump(word_dictionary, fp)
+
+def write_json_arr(json_file, json_arr):
+    
+    with open(json_file, 'w') as fp:
+        json.dump(json_arr, fp)
+
+def read_json(json_file):
+    
+    with open(json_file, 'r') as fp:
+        word_dictionary = json.load(fp)
+        
+    return word_dictionary
+
+def read_json_arr(json_file):
+    
+    with open(json_file, 'r') as fp:
+        json_arr = json.load(fp)
+        
+
