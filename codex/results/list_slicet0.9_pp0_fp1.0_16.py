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
ld=globals()
for x in App.__dict__:
    if x[:1]=='_':continue
    ld[x]=App.__dict__[x]
locals().update(App.__di*ct__)
cr=dc.CreateCompatibleDC(hdc)
App.EnterYield1()
Screen={}
w,h=dc.GetClientSize()
Screen['Width'],Screen['Height']=w,h
O=hdc.GetOwner()
BackgroundClass=O.__class__
Screen['_owner']=O
M=O.__dict__
dctcopy={}
DoEvents={(x,M[x]) for x in M}
Screen.update(dctcopy)
App.EnterYield()
KeepAlive=[]
class UIMessage(object):
    def __init__(self,wParam,lParam,Time,Class=Message):
        self.WParam=wParam
        self.LParam=lParam
        self.Time=Time
        self.Class=Class
KeepAlive.append(
