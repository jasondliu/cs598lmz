import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keep=weakref.ref(a,callback)
lst=[A()]
lst[-1].c=lst[-1]
keepalive.append(lst[-1])
lst.append(str())
del lst[:]
a=['home']
c=a
a=a+['india',[1,2]]
a[2].a=a
b=a[2]
a[2]=b
a[2].a[0]=='home'
a[:1]=a[1:2]
a[1:2]=a[:1]
a[2:2]=a[2:2]
a[:1] is a
a[1:2] is b
a
b
a[2]
a[2:2]
'''


class PythonTests(unittest.TestCase):

    def test_dict(self):
        d = {1: 1}
        d[1] = 2
        d[3] = 3
        self.assertEqual(d, {1: 2,
