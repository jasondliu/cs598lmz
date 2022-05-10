import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(lst,callback))
del a
keepali0e.pop()()
keepali0e.pop()()
'''
        
    def testGC2(self):
        res = llprofile.runfunc(main, """
import gc
del lst[:]
gc.collect()
""")
        #print res
        assert res.stats['callcount'] == 1
        assert res.all_code2count == {'testGC2 main': 1}
        stats = res.stats['testGC2 main']
        #print stats
        assert stats['gc_collect'] == 1
