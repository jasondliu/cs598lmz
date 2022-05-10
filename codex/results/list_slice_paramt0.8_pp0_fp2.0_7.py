import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
if lst:print lst[0]
else:print "NONE"
lst=None
if lst:print lst[0]
else:print "NONE"

'''

COMMENT_SUMMARY = \
'''
Comment Summary:

'''

def p(string):
    print string
    return string

def iter_examples(reg):
    reg.awake = True
    reg.filter_full_match = True
    while not (reg.is_closed or reg.is_empty):
        yield reg.readline()

def exercise_0(reg):
    '''
    >>> reg['foo'] = 'bar'
    >>> print reg['foo']
    bar
    '''
    reg['foo'] = 'bar'
    print reg['foo']
    
def exercise_1(reg):
    '''
    >>> reg['foo'] = 'bar'
    >>> del reg['foo']
    '''
    reg['foo'] = 'bar
