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
lst.append(lst)
lst=None
try:
	while 1:keepali0e.append(str())
except MemoryError:
	sys.stdout.write("\n"*256+"3")
else:raise SystemExit
""")
		self.assertEqual(output.getvalue(),expected)
	@unittest.skipIf(sys.platform.startswith("java"), "TODO Jython implementation of weakrefs")
	def test_int_weakref(self):
		# https://bugs.python.org/issue32501#msg327445
		# Bug was that when `callback` was called, there was no way to get the weak dictionary of 3 or 42, and
		#  no way to delete the ref.
		codestr="""
from weakref import ref

d = {'foo': 3}
def callback(x):
    if x is 3:
        d.pop('foo')

def baz():
    d['foo'] = 42

def foo():
    for _ in range(
