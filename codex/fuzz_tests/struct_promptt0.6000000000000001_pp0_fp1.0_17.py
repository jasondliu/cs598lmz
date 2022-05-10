import _struct
# Test _struct.Struct.format_size()
with _struct.Struct('i') as s:
    assert s.format_size() == 4
    assert s.size == 4
with _struct.Struct('ii') as s:
    assert s.format_size() == 8
    assert s.size == 8
with _struct.Struct('iii') as s:
    assert s.format_size() == 12
    assert s.size == 12
with _struct.Struct('iiii') as s:
    assert s.format_size() == 16
    assert s.size == 16
with _struct.Struct('iiiii') as s:
    assert s.format_size() == 20
    assert s.size == 20
with _struct.Struct('iiiiii') as s:
    assert s.format_size() == 24
    assert s.size == 24
with _struct.Struct('iiiiiii') as s:
    assert s.format_size() == 28
    assert s.size == 28
with _struct.Struct('iiiiiiii') as s:
    assert s.format_size() == 32
   
