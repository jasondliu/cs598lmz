import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a_wr=weakref.ref(a,callback)
while keepalive:lst.append(lst[0])"

_res=_("""

""")

_TESTS.append({ 'id':'weakref_bug', 'description':_description, 'pattern':_pattern, 'expected':_res, 'type':'fail' })

#############################################################################
#
#		Test for co_xxx fields in the code object
#
############################################################################

_description=_("""
""")

_pattern="[ x.co_xxx for x in [x for x in dir(type) if x.startswith('co_')]]"

_res=_("""

""")

_TESTS.append({ 'id':'code_attr', 'description':_description, 'pattern':_pattern, 'expected':_res, 'type':'fail' })

#############################################################################
#
#		Test for getattr(object, name, default=None)
#
################################
