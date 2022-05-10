import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]

# test_weakref_callbacks.py
#
#  Copyright (c) 2005-2020, Enthought, Inc.
#  All rights reserved.
#
#  This software is provided without warranty under the terms of the BSD
#  license included in LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
#

"""
Test weakref callbacks.

Note: This test is also used to test weakref callbacks in Python 2.
"""

import gc
import weakref


class A(object):
    def __init__(self, callback):
        self.callback = callback

    def __del__(self):
        self.callback()


def test_callback_is_called():
    called = []

    def callback():
        called.append(True)

    a = A(callback)
   
