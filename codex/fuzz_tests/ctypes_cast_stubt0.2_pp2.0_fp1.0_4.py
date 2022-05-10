import ctypes
ctypes.cast(0, ctypes.py_object)

# SEGV

import ctypes
ctypes.cast(0, ctypes.py_object).value

# SEGV

import ctypes
ctypes.cast(0, ctypes.py_object).value = 0

# SEGV

import ctypes
ctypes.cast(0, ctypes.py_object).ob_refcnt

# SEGV

import ctypes
ctypes.cast(0, ctypes.py_object).ob_refcnt = 0

# SEGV

import ctypes
ctypes.cast(0, ctypes.py_object).ob_type

# SEGV

import ctypes
ctypes.cast(0, ctypes.py_object).ob_type = 0

# SEGV

import ctypes
ctypes.cast(0, ctypes.py_object).ob_size

# SEGV

import ctypes
ctypes.cast(0, ctypes.py_object).ob_size = 0

# SEGV
