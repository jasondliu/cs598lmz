import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]=a
lst=None
del keepali0e
b=A()
b.c=b
AliasIssue.reportAliasIssue(b)


"""
"""

class AliasIssue(object):
    aliasList = set([])
    def reportAliasIssue(self, clsInstance):
        for aliasName in clsInstance.__dict__.keys():
            if isinstance(getattr(clsInstance, aliasName), clsInstance.__class__):
                print 'ERROR: Severe Aliasing Issue detected in class %s' % (aliasName,)
                print '       This type of aliasing is known to cause all manner of problems'
                self.aliasList.add((aliasName, clsInstance.__class__.__name__))

import weakref
class A(object):
    pass
def callback(x):
    print x
    AliasIssue.reportAliasIssue(x)

a = A()
a.b = a
print 'end of allocation'


"""
"""
class AliasIssue(object):
	aliasList
