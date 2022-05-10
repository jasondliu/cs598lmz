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
print len(keepali0e)

#----------------------

lst=[]
lst.append(lst)
print len(lst)

#----------------------

print []+[]

#----------------------

lst=[]
lst.append(lst)
print lst[0] is lst

#----------------------

print [] is not []

#----------------------

lst=[]
lst.append(lst)
print lst[0] is lst

#----------------------

lst=[]
lst.append(lst)
print lst is lst[0]

#----------------------

lst=[]
lst.append(lst)
print lst[0] is lst

#----------------------

lst=[]
lst.append(lst)
print lst is lst[0]

#----------------------

lst=[]
lst.append(lst)
print lst[0] is not lst

#----------------------

lst=[]
lst.
