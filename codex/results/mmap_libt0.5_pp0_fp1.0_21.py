import mmap
+import os
+import re
+import sys
+import time
+
+from collections import Counter
+from itertools import chain, combinations
+from optparse import OptionParser
+from pprint import pprint
+from subprocess import Popen, PIPE
+
+
+def get_words(file):
+    '''
+    Return an array of words in a file
+    '''
+    words = []
+    with open(file, 'r') as f:
+        for line in f:
+            words.extend(line.split())
+    return words
+
+
+def get_word_count(file):
+    '''
+    Return a dictionary of words and their counts in a file
+    '''
+    return Counter(get_words(file))
+
+
+def get_word_count_mmap(file):
+    '''
+    Return a dictionary of words and their counts in a file
+    '''
+    with open(file, 'r') as f:
+        words = mmap
