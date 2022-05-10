fn = lambda: None
# Test fn.__code__.co_filename and fn.__code__.co_firstlineno

# Cannot test filenames: files could be converted to bytecode.
# Cannot test line numbers: bytecode and source could be out of sync.

print 'Test the co_flags member of code objects'

def f1(): pass
print f1.__code__.co_flags & CO_OPTIMIZED

def f2(x=1): pass
print f2.__code__.co_flags & CO_OPTIMIZED

def f3(): global g
print f3.__code__.co_flags & CO_OPTIMIZED

def f4(x=[]): pass
print f4.__code__.co_flags & CO_OPTIMIZED

def f5():
    def g():
        pass
print f5.__code__.co_flags & CO_OPTIMIZED

def f6():
    class C:
        pass
print f6.__code__.co_flags & CO_OPTIMIZED

def f7():
