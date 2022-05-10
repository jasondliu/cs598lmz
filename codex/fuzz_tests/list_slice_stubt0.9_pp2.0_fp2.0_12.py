import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=callback
i=0
while i<1000:a.c=a.b=a.a=a;i+=1
while i<10000:a.c=a.b=a.a;i+=1
a.c=a.b=a.a=keepali0e
a.c=a.b=a.a=a
a.c=a.b=a.a=callback
del a.c,a.b
while a.a:pass
del a.a
gc.collect()
```

```c
//sys.stdout.reconfigure(encoding='utf_8')
//python.exe - an unusual interpreter process
//"python.exe" - an unusual file
//"python.exe" - a process you don't recognize
//Output: "python.exe" - an unusual interpreter process
//An unusual interpreter process: "python.exe"
//python.exe - an unknown interpreter
//python.exe - an unknown interpreter - a process you don't recognize
//"python.exe" - an unusual interpreter process

```
