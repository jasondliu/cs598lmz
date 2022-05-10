import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
del a
a=A()
a.c=A()
keepali0e.append(weakref.ref(a.c))
del a

"""

def parse_gc_callback(text):
   

    lines = text.split('\n')
    callback = []
    keepalive = []
    for line in lines:
        x = line.split('=')
        if 'keepalive' in line:
            x = keepalive
        elif 'call' in line:
            x = callback
        else:
            x = None
        if x:
            name = x[0]
            x = x[1]
            x = ''.join(list(filter(lambda c:c.isdigit(),x)))
            x = list(map(int,x))
            globals()[name].extend(x)
    
    
    


parse_gc_callback(text)
keepalive,callback

import gc
gc.set_callback(callback.pop)
while callback:
    gc.collect()
   
