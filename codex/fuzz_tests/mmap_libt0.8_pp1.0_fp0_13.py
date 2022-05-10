import mmap
+from datetime import datetime
+
+def add(x, y):
+   return x + y
+
+def writeFile(fileName, text):
+   f = open(fileName,'w')
+   f.write(text)
+   f.close()
+
+def readFile(fileName):
+   f = open(fileName,'r')
+   text = f.read()
+   f.close()
+   return text
+
+def getMapFor(fileName):
+   f = open(fileName,'r')
+   text = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+   #text = mmap.mmap(f.fileno(), 50)
+   f.close()
+   return text
+
+
+def mmap_test():
+   text = 'Testing '
+   text = text * 100000
+   fileName = 'testMmap.txt'
+   writeFile(fileName, text)
+   map = getMapFor
