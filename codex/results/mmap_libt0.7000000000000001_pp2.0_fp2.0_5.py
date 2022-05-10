import mmap
+
+#read file
+f=open("test.txt","r+")
+
+#mmap the file
+m=mmap.mmap(f.fileno(),0)
+n=m.size()
+
+#write to the file
+m.resize(n+1000)
+m.write("Yaren")
+
+#read from the file
+m.seek(0)
+print m.readline()
+
+#close file
+m.close()
+f.close()

