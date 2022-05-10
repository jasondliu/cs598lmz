gi = (i for i in ())
# Test gi.gi_code
assert type(gi.gi_code) is types.CodeType
# Test gi.gi_frame
assert type(gi.gi_frame) is types.FrameType


def f():
    gi = (i for i in ())
    # Test gi.gi_code
    assert type(gi.gi_code) is types.CodeType
    # Test gi.gi_frame
    assert type(gi.gi_frame) is types.FrameType


f()

# Test mappings

# Test mappingproxy
l = [1, 2, 3]
mp = types.MappingProxyType(l)
# Test mp[0]
assert mp[0] == 1
# Test mp[1]
assert mp[1] == 2
# Test mp[2]
assert mp[2] == 3

# Test general __dir__
assert dir(mock_obj) == sorted(
    [
        "__abs__",
        "__add__",
        "__and__",
        "__bool__",
        "__call__",
        "__class__",
