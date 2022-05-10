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
try:print(lst)
finally:del lst
keepali0e.clear()
try:print(lst)
finally:del lst
 
keepali0e.append(str())
try:print(lst)
finally:del lst
keepali0e.append(str())
try:print(lst)
finally:del lst
keepali0e.append(lst)
try:print(lst)
finally:del lst
keepali0e.clear()
try:print(lst)
finally:del lst

topic='keepali0e'
list=dir(__builtins__)
if not list:list=[]
print("Bruno's "+topic+'->',list,"\n")
del list
 
topic=''
list=dir(__builtins__)
if not list:list=[]
print("Bruno's "+topic+'->',list,"\n")
del list
 
topic='del'
list=dir(__builtins__)
if not list:list
