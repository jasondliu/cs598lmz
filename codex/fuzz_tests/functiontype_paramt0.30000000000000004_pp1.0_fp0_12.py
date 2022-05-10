from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Issue #15: http://code.google.com/p/python-virtualenv/issues/detail?id=15
# This test is not applicable to PyPy
if not hasattr(sys, 'pypy_version_info'):
    import virtualenv
    virtualenv.create_bootstrap_script('foo')

# Issue #16: http://code.google.com/p/python-virtualenv/issues/detail?id=16
import virtualenv
virtualenv.create_environment('foo', site_packages=True)

# Issue #17: http://code.google.com/p/python-virtualenv/issues/detail?id=17
# This test is not applicable to PyPy
if not hasattr(sys, 'pypy_version_info'):
    import virtualenv
    virtualenv.create_environment('foo', site_packages=False)

# Issue #18: http://code.google.com/p/python-virtualenv/issues/detail?id=18
import virtualenv
virtualenv.create_environment
