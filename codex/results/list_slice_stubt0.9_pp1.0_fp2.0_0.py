import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive=keepalive.append(lst)
lst[0].c=lst[1]
A().c=lst[1]
keepalive=keepalive.append(lst)

import weakref
import threading

class Outer(object):
	class Inner(object):
		pass

tasks=[]

def worker():
	for _ in range(20):
		o=Outer()
		tasks.append(o)
	time.sleep(1)

def main():
	thread=[threading.Thread(target=worker) for _ in range(5)]
	for t in thread:
		t.daemon=True
		t.start()
	for t in thread:
		t.join()

if __name__=='__main__':
	main()
