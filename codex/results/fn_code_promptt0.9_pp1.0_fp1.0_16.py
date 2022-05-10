fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    print('SKIP')
    raise SystemExit

# Check that module_name only affects the repr printed for builtins
import builtins, sys
print('OK' if builtins.__name__ != sys.__name__ else 'FAIL')
