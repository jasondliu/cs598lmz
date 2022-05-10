import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
weakref.ref(a,callback)

#----------------------------------------------------------------------

#writepyc.py

#----------------------------------------------------------------------

'writes a .pyc file from a .py file'

import imp,marshal,new,os,struct,sys
MAGIC=imp.get_magic()

def makepyc(pyfile,pycfile=None):
    filename=pyfile.name
    code=compile(pyfile.read(),filename,'exec')
    fc=getattr(code,'co_firstlineno',None)
    if fc is None:fc=0
    mtime=os.stat(filename).st_mtime
    if pycfile is None:
        pycfile=filename+'c'
    fc=(fc<<16)+(mtime&0xFFFF)
    fc=struct.pack('<I',fc)
    with open(pycfile,'wb') as fcfile:
        fcfile.write(MAGIC+fc+
        marshal.dumps(code))

