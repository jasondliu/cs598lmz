import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a hack to get around the fact that the Python 2.7.3
# interpreter crashes when ctypes.py_object is passed between
# interpreters.
import sys
if sys.version_info[:3] == (2, 7, 3):
    import platform
    if platform.python_implementation() == 'CPython':
        raise NotImplementedError('Python 2.7.3 is not supported due to a bug in the Python interpreter. See\n'
                                  'https://github.com/uqfoundation/multiprocess/issues/152\n'
                                  'for more information.')

#
# Copyright (c) 2006-2012
# Anthony Scopatz - https://github.com/scopatz/multiprocess
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions
