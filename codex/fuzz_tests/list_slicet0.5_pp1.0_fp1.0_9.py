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
import gc
gc.collect()
print keepali0e

def main():
    print "this is main"

def test():
    print "this is test"

if __name__ == "__main__":
    print "this is __name__"
    main()
    test()

import os
import sys

#print os.path.join(os.path.dirname(__file__),'..')
#print os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
#print sys.path[0]
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
#print sys.path
#print os.path.dirname(__file__)
#print os.path.abspath(os.path.dirname(__file__))
#print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print os
