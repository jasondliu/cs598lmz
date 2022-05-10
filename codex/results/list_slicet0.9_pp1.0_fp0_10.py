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
del  lst, keepali0e
lst
del lst
a.c


#mem



##################################################################################

import resource
def closeall():for fd in range(3,256):try:os.close(fd)
except OSError:pass
def spawn(argv):if sys.platform == 'os2emx':closeall()
else:maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
if maxfd == resource.RLIM_INFINITY:maxfd = 256
for fd in range(3, maxfd):try:os.close(fd)
except OSError:pass
os.execv(argv[0], argv)
def spawnv(path, argv):if sys.platform == 'os2emx':closeall()
else:maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
if maxfd == resource.RLIM_INFINITY:maxfd = 256
for fd in range(3, maxfd):try:os.close(fd
