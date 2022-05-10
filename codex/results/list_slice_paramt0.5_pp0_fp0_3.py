import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(str())
a.c=lst
keepali0e.append(weakref.ref(a,callback))
del lst,a
del keepali0e
import gc
gc.collect()

"""
    output = _dci.cmdexec(stmt)
    _dci.expect_complete_msg(output)
    #
    #  Expect the first element of lst to be deleted.
    #
    stmt = """values (length(lst));"""
    output = _dci.cmdexec(stmt)
    _dci.expect_file(output, defs.test_dir + """/a01exp""", 'a01s5')
    #
    #  Expect the second element of lst to be deleted.
    #
    stmt = """values (length(lst));"""
    output = _dci.cmdexec(stmt)
    _dci.expect_file(output, defs.test_dir + """/a01exp""", 'a01s6')
   
