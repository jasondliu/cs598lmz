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

### import weakref,objgraph
### objgraph.show_backrefs(objgraph.by_type('dict')[-1],filename='a.png')
###
### d=weakref.WeakValueDictionary()
### d[1]=[]
### d[2]=[]
### d[3]=[]
### d[4]=[]
### d[1]=[1,2]
### d[2]=[1,2]
### d[3]=[1,2]

### list=[]
### list.append(list)
### del list

### import gc,threading
### a=[]
### def run():
###     gc.collect()
###     import objgraph
###     objgraph.show_backrefs([obj for obj in gc.get_objects() if isinstance(obj,dict)][0],filename='%s.png'%threading.currentThread().getName())
### xxx=threading.Thread(target=run)
### xxx.start()
### del xxx

### import weakref,gc,objgraph
###
