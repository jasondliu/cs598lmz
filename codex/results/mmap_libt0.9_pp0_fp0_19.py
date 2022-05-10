import mmap
+
+def load_dic_stops():
+    """
+    load stop word list and make them as a dict type
+    """
+    global dic_stops
+    dic_stops = {}
+    #filename = 'stopwords.dat'
+    filename = '../CN/stopword.csv'
+    for line in open(filename):
+        line = line.strip()
+        dic_stops[line] = 1
+    #print(dic_stops)
+
+def tag_words(line):
+    """
+    1. filter out all stop words and punct
+    2. filter out all items whose length is less than 2 and whose 1st and 2nd char are same
+    3. transform to lower case
+    """
+    word_lst = []
+    seg_list = jieba.cut(line, cut_all=False)
+    #seg_list = jieba.cut(line, cut_all=True)
+    #seg_list = jieba
