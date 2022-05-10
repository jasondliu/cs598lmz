import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]+=a



# lst=[a]
# # print(lst.index('a'))
# lst[0]='a'
# print(lst)


# a=sum([],1)
# print(type(a))


# a='111'
# b='111'
# print(id(a)==id(b))
# del b

# # a=A()
# b='1'
# del a
# # print(a.__dict__)
# a=A()
# a.__dict__['b']=2
# print(a.__dict__)


# a=A()
# keepalive=[a]
# keepalive[0]=[]

# del a

# id(a)

# a=A()
# b=A()
# print(id(a),id(b))
# a=1
# b=1
# print(id(a),id(b))


# c=a
# print(id(a),id(
