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
'''

def optimize(source,target,mix_source=True,**options):
    m=_optimize(source,target,mix_source)
    m.mainloop(**options)
    return m.to_source()

def mainloop(source,target,mix_source=True,**options):
    m=_optimize(source,target,mix_source)
    m.mainloop(**options)

if __name__=='__main__':
    if len(sys.argv)==3:
        source_file,target_file=sys.argv[1:3]
    elif len(sys.argv)==2:
        source_file=sys.argv[1]
        target_file=None
    else:
        print('python -mfennel.optimize <source file> [<target file>]')
        exit(1)

    with open(source_file,'r') as f:
        source = f.read()
    if target_file is None:
        target = source
    else:
        with
