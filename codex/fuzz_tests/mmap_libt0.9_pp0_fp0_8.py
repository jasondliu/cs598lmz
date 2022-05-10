import mmap
+from traceback import print_exc
+from time import time
+
+import sys
+
+def is_immutable(o):
+	try:
+		o[:]=o
+	except:
+		return True
+	return False
+
+raise Exception()
+
+c=0
+
+def r(o,a=0):
+	global c
+
+	c+=1
+	
+	print(c,o,type(o),a)
+
+	try:
+		for i in o:
+			r(i,a+1)
+	except:
+		if not is_immutable(o):
+			r(list(o),a+1)
+	
+t=[
+	lambda x: x==5,
+	lambda x: x!=5,
+	lambda x: x>5,
+	lambda x: len(x)==5,
+	lambda x: len(x)!=5,
+	lambda x: len(
