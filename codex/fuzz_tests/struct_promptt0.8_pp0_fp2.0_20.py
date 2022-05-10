import _struct
# Test _struct.Struct and all known format characters
for code in 'xcbB?hHiIlLqQfdP':
    try:
        # Common case
        size = _struct.calcsize(code)
        _struct.Struct(code)
    except ValueError:
        # This format character can't be used alone
        pass
    except _struct.error:
        # Invalid format character
        print('invalid format character: %c' % code)

# Issue #18574: Test the '@' character.
try:
    _struct.Struct('@')
except _struct.error:
    pass
# Issue #18574: Test any format character followed by '@'.
for code in 'cbB?hHiIlLqQfdP':
    try:
        size = _struct.calcsize(code + '@')
        _struct.Struct(code + '@')
    except ValueError:
        # This format character can't be used alone
        pass
    except _struct.error:
        print('invalid format character: %c' % code)
