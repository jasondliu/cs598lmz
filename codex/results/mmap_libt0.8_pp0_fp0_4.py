import mmap
+import re
+
+# Create a list of words to omit from the wordcloud
+omitWords = ['this','that','have','from','with','will','your','you','were','had','has','which','their','there','when','what','who','them','can','each','than','were','him','into','been','same','make','most','some','must','like']
+
+
+def punctuationtokenizer(s):
+    """
+        Given a string, returns a list of words seperated by punctuation.
+        Words have been further cleaned by removing digits, spaces, and 
+        user defined words to omit.
+    """
+    tokens = re.sub("[^\w]+"," ",s).lower().split()
+    return [re.sub("[0-9]","" , i) for i in tokens if i not in omitWords]
+
+def loadtext(fname):
+    """
+        Given a file name, create an iterator of lines of text.
+        This is an alternative to the readlines() method, which
+
