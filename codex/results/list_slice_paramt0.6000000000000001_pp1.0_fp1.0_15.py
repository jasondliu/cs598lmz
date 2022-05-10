import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
del a
print keepali0e
print lst

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
del a
print keepali0e
print lst

#list_str_str
print [str()]

#list_class_str
print [str]

#list_str_class
print [str()]

#list_class_class
print [str]

#list_str_list_str_str
print [str(),str()]

#list_str_list_class_str
print [str(),str]

#list_str_list_str_class
print [str(),str()]

#list_str_list_class_class
print [str
