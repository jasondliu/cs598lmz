import types
types.IntType

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys;

def fibonacci(n):
    if n<2:
        return n;
    else:
        return (fibonacci(n-1)+fibonacci(n-2));
