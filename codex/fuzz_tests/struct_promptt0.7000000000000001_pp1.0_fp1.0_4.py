import _struct
# Test _struct.Struct.format_size() on native alignment rules.
with warnings.catch_warnings(record=True) as w:
    ss = _struct.Struct('i')
    ss.format_size(True)
    assert len(w) == 0
with warnings.catch_warnings(record=True) as w:
    ss = _struct.Struct('H')
    ss.format_size(True)
    assert len(w) == 0
with warnings.catch_warnings(record=True) as w:
    ss = _struct.Struct('3s')
    ss.format_size(True)
    assert len(w) == 0
with warnings.catch_warnings(record=True) as w:
    ss = _struct.Struct('x')
    ss.format_size(True)
    assert len(w) == 0
with warnings.catch_warnings(record=True) as w:
    ss = _struct.Struct('xx')
    ss.format_size(True)
    assert len(w) == 0
# Test _struct.Struct.format_size() on non-
