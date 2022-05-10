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
</code>
When I change the final line in the code to 
<code>while lst:print "pre - len(lst)=",len(lst),"id=",id(lst[0])," : ", hex(id(lst[0])), " : ", lst[0]
</code>
I get:
<code>pre - len(lst)= 1 id= 31458280  :  0x1f03080  :  ' '
pre - len(lst)= 1 id= 31458280  :  0x1f03080  :  ' of '
pre - len(lst)= 1 id= 31458280  :  0x1f03080  :  ' of of '
pre - len(lst)= 1 id= 31458280  :  0x1f03080  :  ' of of of of '
pre - len(lst)= 1 id= 31458280  :  0x1f03080  :  ' of of of of of of '
pre - len(lst)= 1 id= 31458280  :  0x1f
