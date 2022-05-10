import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
w=weakref.ref(a,callback)
keepalive.append(w)
del a
#print lst

# 弱引用可以用在缓存对象的实现中，或者在对象间建立循环引用时，确保没有游离的循环引用
class Cheese(object):
	def __init__(self,kind):
		self.kind=kind
	def __repr__(self):
		return 'Cheese(%s)'%self.kind
import weakref

stock=weakref.WeakValueDictionary()
catalog=[Cheese('Red Leicester'),Cheese('Tilsit'),Cheese('Brie'),Cheese('Parmesan')]
for cheese in catalog:
	stock[cheese.kind]=cheese
print sorted(stock.keys())
del catalog
print sorted(stock.
