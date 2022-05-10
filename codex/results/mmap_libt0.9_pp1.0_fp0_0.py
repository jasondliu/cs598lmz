import mmap
+
+def load_word2vec(path):
+    # load word2vec
+    vocab = []
+    embd = []
+    file = open(path,'r')
+    for line in file.readlines():
+        row = line.strip().split(' ')
+        vocab.append(row[0])
+        embd.append(row[1:])
+    file.close()
+    return vocab, embd
+
+def load_dictionary(path):
+    # loading dictionary
+    # w2v for word2vec, wp for wrongs, rp for rights
+    tgt = open(path + 'dictionary.txt', 'r')
+    lines = tgt.readlines()
+    wrights = []
+    wrongs = []
+    w2v_idx = []
+    for i in range(len(lines)):
+        splits = lines[i].strip().lower().split('\t')
+        wright = splits[0]
+        wrongs = splits[
