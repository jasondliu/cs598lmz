import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(A)
lst.append(a)
del a
lst.append(str())
lst.append(str())
lst.append(str())
lst.append(str())
n=1005
while n:lst.append(n);n-=1
print "len(lst): ",len(lst)
weakref.ref(lst,callback)
del lst
del weakref

result = test.exec_sql(_dci.cmdexec(stmt))
_dci.expect_prepared_msg(output)
output = _dci.cmdexec("""execute XX;""")
_dci.expect_error_msg(output, '8401')

# PASS:0086 If ERROR, rowcounts = 1?

# make sure values are correct

# PASS:0087 If value of rowcounts = 1?

# END TEST >>> 0086 <<< END TEST
