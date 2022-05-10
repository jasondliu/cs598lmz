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
 if have_unic0de:
  del lst
print keepali0e
del keepali0e
"""

def calc_cython_test(test):
    """Run a cython test, and return the output,
    None if successful, or a string with a message if test fails"""
    import os, py_compile
    fname = py_compile.compile(test)
    outf = os.tmpfile()

    try:
        os.system("cython -a %s 2>&1 | tee %s" % (fname, outf.name))
        outf.seek(0)
        out = outf.read()
        if os.path.isfile(fname + ".so"):
            whocares = os.system("rm %s" % (fname + ".so"))
        if os.path.isfile(fname + ".c"):
            whocares = os.system("rm %s" % (fname + ".c"))
    finally:
        os.unlink(fname)
        outf
