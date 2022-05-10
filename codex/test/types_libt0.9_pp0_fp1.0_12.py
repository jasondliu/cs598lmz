import types
types.StringTypes

print (isinstance("a String", StringTypes))

print(Cls.GetTest)

Cls.GetTest = staticmethod(Cls.GetTest)

print(Cls.GetTest)

print("\n------------------------\n")

class A:
	def __init__(self):
		print("A")
	
	def printA(self):
		print("print A")
	
	@staticmethod
	def StaticFunc():
		print("Static func")
		
	@classmethod
	def ClassMethod(cls):
		print("class method")
		
a = A()

A.ClassMethod()

class B(A):
	def __init__(self):
		print("B")
	
	def printB(self):
		print("print B")
		
b = B()

