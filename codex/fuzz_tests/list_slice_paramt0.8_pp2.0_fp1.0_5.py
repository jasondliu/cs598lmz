import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(a.c,callback))
del a,A
while len(keepali0e):
    keepali0e.pop()()
	
	
	
	
class Base(object):
    def __init__(self):
        self.keep_alive = self
    def __del__(self):
        print 'Base.__del__()'
class A(object):
    def __init__(self):
        self.keep_alive = Base()
    def __del__(self):
        print 'A.__del__()'
a = A()
a.keep_alive = None
del a
	
	
	
	
	
	
#=================python游戏引擎=================
#使用前先安装库pyglet
import pyglet
window = pyglet.window.Window() #创建一个窗口
label = pyglet.text.Label('Hello, world',

