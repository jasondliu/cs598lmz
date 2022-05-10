import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=A()
a.e=a
a.name=a
a.t=A()
a.t.callback=callback
lst[0]=a
keepalive.append(lst)
</code>
here's the output of heapy (the only thing i needed to change was the class name (in order to have gc run when i needed it) :
<code>(Pdb) import code
(Pdb) code=code.strip()
(Pdb) exec(code)
(Pdb) h=heapy.heap()
(Pdb) h.dominate()
Partition of a set of 495 objects. Total size = 12400 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0       1   0 12232   99 12232   99 list
     1       1   0   132    1 12363  100 str
     2       1   0    17    0 12380  100 dict (no owner)
     3       1   0    17    0 12397  100 type
</code>
here
