import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])'''

# print '\n'.join([get_random_string(100) for x in xrange(100)])


# print '\n'.join([get_random_string(100) for x in xrange(100)])
# print get_random_string(100)


#!/usr/bin/python
# -*- coding: utf-8 -*-

# ###############################################################################
#
# Так как многие функции в этом модуле вызываются из командной строки, для
# предотвращения ошибок необходимо чтобы к ним всегда были передан
