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
id(keepalive)
import os,mmap
def memory_map(filename,access=mmap.ACCESS_WRITE):size=os.path.getsize(os.path.join(os.getcwd(),filename))
fd=os.open(filename,os.O_RDWR)
return mmap.mmap(fd,size,access=access)

with open(r'C:\Users\Administrator\Desktop\Fun.py','r+') as f:
    m=memory_map(f.name)
    print m.readline()
    print len(m)
    m.seek(0)
    m.write(b'hangge.com\n')
    m.flush()
    m.seek(0)
    print m.readline()
    os.close(m.fileno())
    m.close()    
    
    
    
    
    
    
        
import multiprocessing as mp
def work(a):
    for i in range(0,1000000):
        a=a**2
        if a==
