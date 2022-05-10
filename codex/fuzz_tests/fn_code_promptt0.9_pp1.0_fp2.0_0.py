fn = lambda: None
# Test fn.__code__
tfn.__code__
# Test fn.__code__ not False
tfn.__code__ != False
# Test ||
if tfn.__code__ or fn.__doc__:
    pass

# Test code type with &&
def tfn1(): pass
def tfn2(): pass
myCode = tfn1.__code__ and tfn2.__code__

# Test nested 'and' &&
if tfn.__code__ and tfn1.__code__ and tfn2.__code__: pass

# Test not (!)
# Test not simple
if not tfn.__code__: pass
# Test not negation
if not not tfn.__code__: pass
# Test not (!) of negation
if not not not tfn.__code__: pass
if not not not not tfn.__code__: pass
if not not not not not tfn.__code__: pass
if not not not not not not tfn.__code__: pass
# Test double not (!!)
if not not tfn.__code__: pass
# Test
