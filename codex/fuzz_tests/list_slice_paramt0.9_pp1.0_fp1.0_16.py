import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print "a is still there, but we're done with it:"
print """
try:
    len(lst)
except ReferenceError: "
    text = str(sys.exc_info())"
    pass
else:
    text = 'lst is intact'
"""
print text
del(a)
print "a is gone and list is OK:"
print """
try:
    len(lst)
except ReferenceError: "
    text = str(sys.exc_info())"
    pass
else:
    text = 'lst is intact'
"""
print text
