import ctypes
ctypes.cast(0, ctypes.py_object)

import sys
sys.getrefcount(None)

import sys
sys.getrefcount(1)

import sys
sys.getrefcount(1.0)

import sys
sys.getrefcount("")

import sys
sys.getrefcount("a")

import sys
sys.getrefcount(())

import sys
sys.getrefcount((1,))

import sys
sys.getrefcount([])

import sys
sys.getrefcount([1])

import sys
sys.getrefcount({})

import sys
sys.getrefcount({1:1})

import sys
sys.getrefcount(object())

import sys
sys.getrefcount(object)

import sys
sys.getrefcount(int)

import sys
sys.getrefcount(1)

import sys
sys.getrefcount(1)

import sys
sys.getrefcount(1)

import sys
sys.getrefcount(1)

import sys
