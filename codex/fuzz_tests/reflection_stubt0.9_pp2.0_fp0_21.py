fn = lambda: None
gi = (i for i in ())
fn.__code__ = b''
gi.gi_code = b''

# The following two tests will often trigger an AccessViolation
# exception, which is not easy to catch and test for
# >>> import _testcapimodule
with _pytest.raises(TypeError, match="readonly attribute"):
    fn.__code__ = b''
with _pytest.raises(TypeError, match="readonly attribute"):
    gi.gi_code = b''

# The following two tests will likely trigger a Fatal Python error, which
# is not easy to catch and test for.
# >>> import _testcapimodule
with _pytest.raises(ValueError, match="code"):
    fn.__code__ = b'\x00' * (1 << 18)
with _pytest.raises(ValueError, match="code"):
    gi.gi_code = b'\x00' * (1 << 18)

# attempt to change arguments of builtins
# >>> import _testcapimodule
with _pytest.raises(TypeError, match="readonly
