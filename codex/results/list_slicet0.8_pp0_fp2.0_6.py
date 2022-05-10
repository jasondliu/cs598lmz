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
print len(keepali0e)
EOF
exit 0
*/

#include <Python.h>
#include <stdio.h>
#include <string.h>

struct A {
	PyObject_HEAD
	PyObject *c;
};

static void
traverse(PyObject *obj, visitproc visit, void *arg)
{
	/* Do not access any PyObject member */
	Py_VISIT(obj);
}

static PyObject *
get_count(PyObject *obj, void *closure)
{
	Py_ssize_t count;

	count = Py_REFCNT(obj);
	return PyInt_FromSsize_t(count - 1);
}

static PyObject *
get_weakref(PyObject *obj, void *closure)
{
	PyObject *weakref, *callback, *args;
	struct A *a;

	a = (struct A *) obj;

	callback = a->c;
	if (callback == NULL)
		Py_RETURN_NONE;

	args =
