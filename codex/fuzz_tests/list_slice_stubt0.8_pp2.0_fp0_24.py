import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(A())
lst.append(lst)
lst.append(a)
lst.append(A())
if not is_64_bit():
    assert is_valid_address(id(lst))
    print "got expected assertion, but the test is not valid on 32-bit systems: %s"%(lst,)
else:
    a=lst[-1]
    a.b=a
    lst.append(a)
    lst[2].append(lst)
    del lst[:]
    assert not is_valid_address(id(lst))
    print "no crash, but is_valid_address() returned True on an invalid address, but the test is not valid on 32-bit systems"
del lst
