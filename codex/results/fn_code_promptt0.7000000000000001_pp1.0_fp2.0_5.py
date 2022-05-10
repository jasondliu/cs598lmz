fn = lambda: None
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test versions of Python < 2.6
if not hasattr(fn.__code__, 'co_flags'):
    fn.__code__.co_flags = 0

def test_cannot_overwrite_builtins():
    def bad_builtin_overwrite():
        import builtins
        builtins.open = lambda x: x
    # Test versions of Python <= 2.6
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins
    assert not hasattr(builtins, 'open')
    assert_raises(AttributeError, bad_builtin_overwrite)

# Test sys.modules["__builtin__"]
import sys
sys.modules["__builtin__"] = sys.modules["__builtin__"]

def test_cannot_overwrite_import():
    # Test versions of Python < 2.6
    if not hasattr(fn.__code__, 'co_flags'):
        raise SkipTest("test_cannot_
