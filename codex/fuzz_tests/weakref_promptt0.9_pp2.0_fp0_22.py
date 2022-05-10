import weakref
# Test weakref.ref()

class A:
    pass


a = A()
print(a)
b = weakref.ref(a)
print(b)
print(b())
print(dir(b))
sys.stdout.flush()
del a
#print(b)
#print(b())
#print(dir(b))
sys.stdout.flush()
#test callable
import types
aList = []
class A:
	def __init__(self):
		aList.append(self)
		pass

	def __call__(self):
		print('call : A')
		
class B(A):
	def __call__(self):
		print('call : B')
		pass

aList.append(A())
b = B()
print(b)
print('Is A callable', callable(A))
print('Is B callable', callable(B))
print('Is a callable', callable(aList[0]))
print('Is b callable', callable(b))
print(type(
