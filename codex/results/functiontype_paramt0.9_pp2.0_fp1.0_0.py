from types import FunctionType
list(FunctionType() for i in range(10))

# hasattr, getattr, setattr, delattr
hasattr(Point, 'foo')
hasattr(p, 'x')
getattr(Point, 'foo', 'default')
getattr(p, 'x')
setattr(Point, 'foo', 'bar')
setattr(p, 'x', 3)
delattr(Point, 'foo')
delattr(p, 'x')

# logging
logging.debug('foo')
logging.error('no')
logging.info('bar')
logging.warning('bah')

# math
math.sin(math.pi)
math.sqrt(42)

# re
re.match(r'T', 'Test')
re.search(r'T', 'Test')

# sys
lambda: sys.argv
lambda: sys.byteorder
lambda: sys.copyright
lambda: sys.version
lambda: sys.version_info
lambda: sys.hexversion
lambda: sys.prefix

# time
time.time()
time.clock()

#
