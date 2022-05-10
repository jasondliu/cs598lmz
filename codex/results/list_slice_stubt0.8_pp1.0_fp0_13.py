import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[a]
class ToDump(object):
	def __init__(self,name):self.name=name
	def __del__(self):self.name=''
def get_obj(n):
	if n%2:
		return ToDump(n)
	else:
		return ToDump(n)
def main():
	keepalive=[]
	for i in range(10000):
		obj=get_obj(i)
		keepalive.append(obj)
		if i%3:
			del keepalive[:]
		del obj
		if i%5:
			gc.collect()
if __name__=='__main__':
	main()
