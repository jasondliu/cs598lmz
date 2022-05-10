fn = lambda: None
# Test fn.__code__ is writeable
try:
    fn.__code__ = "foo"
except Exception as e:
    print("ERROR(%s): Could not set fn.__code__ to 'foo': %s"
        % (e.__class__.__name__, e), file=sys.stderr)
    exit(0)
print("fn.__code__ = '%s'" % fn.__code__)
# Test ABI specifier
try:
    ABI = fn.__code__.co_flags & 0xFF
    print("fn.__code__.__flags__ & 0xFF = %d (%s ABI)"
        % (ABI, ["", "PYTHON2", "PYTHON3"][ABI]))
except Exception as e:
    print("ERROR(%s): Could not read fn.__code__.co_flags: %s"
        % (e.__class__.__name__, e), file=sys.stderr)
    exit(1)
# Test calling convention
CC_NAME = fn.__code__.
