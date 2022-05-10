import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=callback
lst[0](lst)
print lst

#[<weakref at 0x7f1b8c1a6c08; to 'list' at 0x7f1b8c1a6d08>]
#[<weakref at 0x7f1b8c1a6c08; to 'list' at 0x7f1b8c1a6d08>]
#[<weakref at 0x7f1b8c1a6c08; to 'list' at 0x7f1b8c1a6d08>]
#[<weakref at 0x7f1b8c1a6c08; to 'list' at 0x7f1b8c1a6d08>]
#[<weakref at 0x7f1b8c1a6c08; to 'list' at 0x7f1b8c1a6d08>]
#[<weakref at 0x7f1b8c1a6c08; to
