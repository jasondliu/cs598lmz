import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=callback
a.e=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(a.c.d)
keepali0e.append(a.e)
del keepali0e[:]
del a
del callback
del lst
'''

LIBPYTHON_NAME = 'libpython2.7.so'
LIBPYTHON_PATH = os.path.join('/usr/lib', LIBPYTHON_NAME)

RANDOM_TIME = 1000 # 1 000ms = 1 second


class GdbHelper:
    def __init__(self, pid, port):
        import gdb
        
        self.gdb = gdb
        
        self.gdb.parse_and_eval('set confirm off')
        self.gdb.execute('attach {0}'.format(pid))
        
        self.gdb.execute('set follow-fork-mode parent')
        self.gdb.execute('set non-stop on')
        
       
