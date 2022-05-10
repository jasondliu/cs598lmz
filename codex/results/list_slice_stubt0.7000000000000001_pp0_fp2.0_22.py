import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
a.b=weakref.ref(a.c,callback)
a.b()
del a
lst[0]
"""
#runcode(code)

#def test_expandtabs():
#    assert 'foo\tbar' == 'foo\tbar'.expandtabs(1)
#    assert 'foo\tbar' == 'foo\tbar'.expandtabs(2)
#    assert 'foo  bar' == 'foo\tbar'.expandtabs(4)

def test_expandtabs_overflow():
    import sys,struct
    chars = [u'\t', u' ', u' ']
    chars.append(u'\t')
    chars.extend([u' ', u' ', u' ', u' '])
    chars.append(u'\t')
    chars.extend([u' ', u' ', u' ', u' '])
    chars.extend([u' ', u' ', u' '])
    s = u''.join(ch
