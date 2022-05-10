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
print 'OK'
EOF

echo -n " OK (using .__del__) ... "
python <<EOF
lst=[str()]
class A(object):
    def __del__(self):
        del lst[0]
a=A()
a.c=a
del a
while lst:lst[:];
print 'OK'
EOF

echo -n " OK (using __delattr__) ... "
python <<EOF
lst=[str()]
class A(object):
    def __delattr__(self,name):
        del lst[0]
        object.__delattr__(self,name)
a=A()
a.c=a
del a
while lst:lst[:];
print 'OK'
EOF

echo -n " OK (using __del__ and __delattr__) ... "
python <<EOF
lst=[str()]
class A(object):
    def __delattr__(self,name):
        del lst[0]
        object.__delattr
