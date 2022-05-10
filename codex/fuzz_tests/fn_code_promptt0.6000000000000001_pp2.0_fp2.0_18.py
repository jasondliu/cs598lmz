fn = lambda: None
# Test fn.__code__
import sys
if sys.version_info[0] >= 3:
    fn.__code__

# Check that the debug mode is not enabled
assert type(fn.__code__) is types.CodeType

# Enable debugging
pydevd.settrace(suspend=False)

# Check that the debug mode is enabled
assert type(fn.__code__) is not types.CodeType

# Disable debugging
pydevd.stoptrace()

# Check that the debug mode is disabled
assert type(fn.__code__) is types.CodeType
