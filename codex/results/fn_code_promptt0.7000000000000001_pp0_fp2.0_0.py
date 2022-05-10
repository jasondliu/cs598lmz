fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    print("SKIP")
    raise SystemExit

# Check that we can create a code block without any of the unsupported
# attributes and it will run fine
code = CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
eval(code)

# Check that an unsupported attribute raises a ValueError
with pytest.raises(ValueError):
    CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', not_an_attr=0)
