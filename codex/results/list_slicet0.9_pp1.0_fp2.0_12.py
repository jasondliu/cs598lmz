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

try:
     _ = compile("for x in range(6): print x\ne\n#x=x+1", '<stdin>', 'exec')
     eval(_)
except SyntaxError:
    assert error.match("invalid syntax")
else:
    assert False, "SyntaxError not raised"

# http://tracker.tinycorelinux.net/index.php?do=details&task_id=1091
omega = u'\u03a9'
if omega != eval("u'"+repr(omega)+"'"):
    print("'%s' != '%s'" % (omega, eval("u'"+repr(omega)+"'")))

# expressions that cannot have leading newlines
for expr in """0
1
"abc
def"
'abc
def'
()
[]
{}
None
True
False
for xx in range(5):pass
while 1:break
if 2:pass
elif 3:pass
else:pass
try:pass
except 4:pass
finally:pass
def f
