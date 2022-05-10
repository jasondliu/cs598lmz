import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#! /usr/bin/env python
# coding=utf-8
class A(object):
    def __init__(self):
        self.a=1
        self.b=2
        self.c=3
        self.d=4
    def __getattr__(self,attr):
        print "getattr:%s"%attr
        return "aaa"
    def __getattribute__(self,attr):
        print "getattribute:%s"%attr
        return object.__getattribute__(self,attr)
    def __setattr__(self,attr,value):
        print "setattr:%s,value:%s"%(attr,value)
        object.__setattr__(self,attr,value)
    def __delattr__(self,attr):
        print "delattr:%s"%attr
        object.__delattr__(self,attr)
    def __getitem__(self,item):
        print "getitem:%s"%item
        return "
