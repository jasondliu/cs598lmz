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
print(keepali0e)
"""
<script>
function gc()
{
var x = Array.prototype.slice.call(arguments);
var y = x.every(function(x){
return x==1;
});
if (y)
{
for (var i = 0; i < 0x1000; i++)
{
var z = [];
for (var j = 0; j < 0x1000; j++)
{
z.push(0x41414141);
}
}
for (var i = 0; i < 0x10; i++)
{
var z = [];
for (var j = 0; j < 0x10000; j++)
{
z.push(0x41414141);
}
}
}
}
function f0()
{
gc(1);
}
function f1()
{
gc(2);
}
function f2()
{
gc(3);
}
function f3()
{
gc(4);
}
function f4()
{
gc(5);
}
function f5()

