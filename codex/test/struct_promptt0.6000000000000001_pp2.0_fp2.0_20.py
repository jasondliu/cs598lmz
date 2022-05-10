import _struct
# Test _struct.Struct.format_size()

# Format string with no alignment directives.
s = _struct.Struct('<I')
assert s.format_size('I') == 4

# Format string with alignment directives.
s = _struct.Struct('<I')
assert s.format_size('IH') == 8

# Format string with alignment directives that are not a power of 2.
s = _struct.Struct('<I')
assert s.format_size('If') == 8

# Format string with alignment directives that are larger than the largest
# alignment directive.
s = _struct.Struct('<I')
assert s.format_size('II') == 8

# Format string with alignment directives that are smaller than the largest
# alignment directive.
s = _struct.Struct('<I')
assert s.format_size('IB') == 5

# Format string with alignment directives that are larger than the smallest
# alignment directive.
s = _struct.Struct('<I')
assert s.format_size('BH') == 4

# Format string with alignment directives that are smaller than the smallest
# alignment directive.
