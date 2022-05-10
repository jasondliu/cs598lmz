import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a

#TODO:Test for stack overflow
#TODO:Test for operation on a weakref after the referent is dead

#TODO:Test for the case where the referent and the weakref are the same object

#TODO:Test for the case where the referent is a weakref to itself

#TODO:Test for the case where the referent is an object that contains a weakref to itself

#TODO:Test for the case where the referent is an object that contains a weakref to itself and a weakref to the referent

#TODO:Test for the case where the referent is an object that contains a weakref to itself and a weakref to the referent

#TODO:Test for the case where the referent is an object that contains a weakref to itself and a weakref to the referent

#TODO:Test for the case where the referent is an object that contains a weakref to itself and a weakref to the referent

#TODO:Test for the case where the referent is an
