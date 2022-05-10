import _struct
+# from _struct import *
+
+
+
+class Base:
+	def __init__ (self, clist):
+		# index = 0
+		self.str = ""
+		for i in clist:
+			print(type(i))
+			print(type(i[0]))
+			self.str = self.str + i[1] + ": " + str(i[0]) + ", "
+
+	def get_str (self):
+		# index = 0
+		print("str: " + self.str)
+
+
+# def pack (fmt, v1, v2, v3):
+def pack ():
+	print("pack")
+
+
+
+class A(Base):
+	def __init__ (self):
+		f1 = (1, "f1")
+		f2 = (2.3, "f2")
+		f3 = ("X", "f3")
+		
