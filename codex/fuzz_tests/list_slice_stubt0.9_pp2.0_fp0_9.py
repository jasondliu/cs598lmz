import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(a.c)
lst[0]='abcde'
lst[0]+=2
lst[0]*=2
lst[0]=lst[0][0:6]
lst[0]+=1

assert len(lst[0])==6
a=A()
a.c=a
b=A()
b.c=b
lst.append(b)
keepali0e.append(b.c)
lst.append(a)
keepali0e.append(a.c)
lst[2]=lst[3]

del keepali0e[0]
callback(lst)
lst[0]

'''DO NOT EXECUTE'''

''' DO NOT EXECUTE '''
