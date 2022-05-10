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
del lst
del lst
print lst
</textarea>
<button id="run" onclick="runit()">run it</button><br/>
<label>use browser console for output</label>
</body>
</html>
