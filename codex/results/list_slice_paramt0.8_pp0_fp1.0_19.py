import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a


# some test of this chapter
# 方法1:
from weakref import WeakKeyDictionary
class Grade(object):
    def __init__(self):
        self._values=WeakKeyDictionary()
    def __get__(self,instance,owner):
        if instance is None:
            return self
        return self._values.get(instance,0)
    def __set__(self,instance,value):
        if not (0<=value<=100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance]=value
class Exam(object):
    math_grade=Grade()
    literature_grade=Grade()
    science_grade=Grade()

#方法2:
import weakref
class Grade(object):
    def __init__(self):
        self._values=weakref.WeakKeyDictionary()
    def __get__(self,instance,owner):
        if instance is None:
            return self
        return self._values.get(instance,0)
   
