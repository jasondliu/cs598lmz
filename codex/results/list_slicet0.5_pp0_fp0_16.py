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
del keepali0e
"""

# python -OO -c "import test; test.run_test(test.test_weakref, -1)"

import sys, os
import unittest
import weakref

class TestWeakref(unittest.TestCase):

    def test_basic(self):
        # Test weak references.
        o = C()
        p = C()
        q = C()
        r = C()
        o.a = p
        o.b = q
        o.c = r
        p.a = o
        p.b = q
        p.c = r
        q.a = o
        q.b = p
        q.c = r
        r.a = o
        r.b = p
        r.c = q
        w = weakref.ref(o)
        self.assertEqual(w(), o)
        self.assertEqual(w().a, p)
        self.assertEqual(w().b, q)
        self.assertEqual(w().c, r)

