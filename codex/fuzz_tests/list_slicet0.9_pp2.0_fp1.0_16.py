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
print(keepali0e)
import operator
class ListTree:
	def __attrnames(self,obj,indent):
		spacing=' ' *(indent+1)
		result=[]
		for attr in dir(obj):
			if attr[:2] =='__' and attr[-2:]=='__':
				result.append(attr)
			else:
				result.append(spacing+attr)
		result.sort(key=str.lower)
		return result;
	def __listclass(self,aClass,indent):
		dots='. . .'
		if indent==0:
			print("Class %s" % aClass.__name__)
		else:
			print("%sClass %s" % (dots[:indent],aClass.__name__))
		for supercls in aClass.__bases__:
			self.__listclass(supercls,indent+4
