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

if __name__=='__main__':
    if 1==len(sys.argv):
        print "Usage: %s argument"%sys.argv[0];
        print "Example: %s 10"%sys.argv[0];
        sys.exit(1);
    else:
        n=int(sys.argv[1]);
        if n>0:
            fib=fibonacci(n);
            print "The "+str(n)+"th fibonacci value is "+str(fib);
