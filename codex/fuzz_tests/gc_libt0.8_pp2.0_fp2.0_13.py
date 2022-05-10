import gc, weakref
import sys, os
from util import *

from Numeric import *



def test(num):
    """
    Create a numpy ndarray and make sure it gives the same answers as
    a builtin list.
    """

    c = array(range(num))
    d = c
    #print id(c),id(d)
    assert c is d
    assert type(c) is type(d)
    assert len(c) == num
    for i in range(num):
        assert c[i] == i
        assert d[i] == i
        assert type(c[i]) is type(d[i])

    print "Passed test 1"

    e = c[0:num]
    #print id(c),id(e)
    assert c is not e
    assert type(c) is type(e)
    assert len(c) == num
    for i in range(num):
        assert c[i] == i
        assert e[i] == i
        assert type(c[i]) is type(e[i])
