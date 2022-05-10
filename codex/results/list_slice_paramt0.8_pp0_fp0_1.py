import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
callback(a)
print(lst,keepali0e)
del a
import gc
gc.collect()
print(lst,keepali0e)

from xml.sax import saxutils,handler
from itertools import chain
class ContentHandler(handler.ContentHandler):
    def __init__(self,target):
        self.target=target
        target.write("<xml version='1.0'>\n")
    def startElement(self,name,attrs):
        target=self.target
        target.write("<"+saxutils.escape(name))
        for a,v in chain(attrs.items(),[("id","_%d"%id(target)
                                         ,"xlink:href","#_%d"%id(attrs)),
                                        ("xlink:rpf","xml")]):
            target.write(" %s='%s'"%(a,v))
        target.write(">")
    def text(self,text):
        self.target.write(saxutils.escape(
