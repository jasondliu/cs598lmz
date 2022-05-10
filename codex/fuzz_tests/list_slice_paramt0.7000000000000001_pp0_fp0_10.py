import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
print(lst[0])

# how to add two lists
lst1 = [1,2,3,4]
lst2 = [5,6,7,8]
lst3 = lst1+lst2
print(lst3)

#what is lambda expression
lst1 = [1,2,3,4]
lst2 = [5,6,7,8]
lst1.append(lambda x,y:x+y)
print(lst1[-1](lst1[0],lst2[0]))

# what is dictionary
dict1={1:'a',2:'b',3:'c'}
print(dict1)

# what are builtin functions
print(dir(__builtins__))

# what is the output of sorted function
dict1 = {1:'a',2:'b',3:'c'}
print(sorted(dict1.keys()))

#what is the difference between range and xrange
for x in range(10):
   
