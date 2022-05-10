import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

keepali0e[-1]
keepali0e[-1]

"""
		keepalive = []
		lst = [str()]
		a = A()
		a.c = a
		keepalive.append(weakref.ref(a, callback))
		del a

		while lst:
			keepalive.append(lst[:])

	def bug_666(self):
		def f():
			raise BaseException
		try:
			f()
		except:
			pass
		finally:
			raise BaseException

	def bug_670(self):
		print('\n'.join((
			"This is a test of the emergency broadcast system.",
			"Please stand by. We are running the test at the request",
			"of the United States Government.",
		)))

	def example_671(self):
		"for name, count in list(items.items()):"
		items = {
