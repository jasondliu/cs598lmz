import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.callback=del_list
del a
del keepalive[0]
assert not lst
def test_extensive_repr_with_dict():
objs=[[],[],(),(),{},{},(),(),[],(),[],([],[],[]),{(1,2):[1,2]}]
for i,obj in enumerate(objs):
s=repr(obj)
assert eval(s),'%r does not evaluate to itself'%s
assert obj==eval(s),'%s does not equal to %s'%(s,obj)
assert type(obj)==type(eval(s)),'%s is not of the same type: %s != %s'%(s,type(obj),type(eval(s)))
def test_repr_recursing():
d={}
d[id(d)]=d
s=repr(d)
assert s=='{%d: {...}}'%(id(d),),'%r != "dummy"'%s
def test_re
