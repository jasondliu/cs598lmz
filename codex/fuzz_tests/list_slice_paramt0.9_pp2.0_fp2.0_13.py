import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,lambda a:callback(a)))

size=0
while True:
    try:lst.append(str(a))
    except TypeError:break
    size+=1
print size

i=0
while lst:
  print i
  i+=1
  print lst.pop().__class__
  print hex(hash(lst[0]))
</code>
For a size of 64868, I get the following output:
<code>64868
0
&lt;type 'str'&gt;
0x7f08032a1c38
1
&lt;type 'str'&gt;
0x7f08032a1538
2
&lt;type 'str'&gt;
0x7f08032a0e38
3
&lt;type 'str'&gt;
0x7f08032a0738
4
&lt;type 'str'&gt;
0x7f08032a0038
5
&lt;type 'str'&gt;
0x7f0803299b38

