import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive=[a]
keepalive.append(weakref.ref(a,callback))
a.a=a
keepalive.append(a)
'''
python2.7 -c 'import gc;gc.enable();import sys;exec(sys.argv[1])' "$python_code"
'''

#3.3.1
python_code='''
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive=[a]
keepalive.append(weakref.ref(a,callback))
a.a=a
keepalive.append(a)
'''

#3.2.2
python_code='''
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]

