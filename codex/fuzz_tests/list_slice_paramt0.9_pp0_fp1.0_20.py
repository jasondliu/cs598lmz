import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
a=A()
keepali0e.append(a)
while keepali0e:pass`
		e := new(Engine)
		e.SetProg(prog)

		e.ExecMain()
	})
}
