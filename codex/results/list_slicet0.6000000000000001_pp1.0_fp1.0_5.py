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
    def test_keepalive_no_cycle(self):
        mod = self.import_extension('foo', [
            ('keepalive_no_cycle', 'METH_NOARGS',
             '''
Py_INCREF(Py_None);
return Py_None;
             '''
            )])
        assert mod.keepalive_no_cycle() is None

    def test_keepalive_cycle(self):
        mod = self.import_extension('foo', [
            ('keepalive_cycle', 'METH_NOARGS',
             '''
PyObject *a, *b;
a = PyList_New(0);
b = PyList_New(0);
PyList_Append(a, b);
PyList_Append(b, a);
Py_DECREF(a);
Py_DECREF(b);
Py_INCREF(Py_None);
return Py_None;
             '''
            )])
        assert mod.keepalive_cycle() is None

    def test_keepalive_
