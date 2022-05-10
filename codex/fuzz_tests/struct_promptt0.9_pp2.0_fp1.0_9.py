import _struct
# Test _struct.Struct error handling.


with _struct.Struct('P') as fmter:
    fmter.iter()  # expecting int size
    fmter.pack()  # expecting int size
    fmter.unpack()  # expecting int size
    with pytest.raises(TypeError):
        fmter.iter('foo')
    with pytest.raises(TypeError):
        fmter.pack('foo')
    with pytest.raises(TypeError):
        fmter.unpack('foo')

with pytest.raises(_struct.error):
    _struct.Struct('Z')  # code not found
with pytest.raises(_struct.error):
    _struct.Struct('P', 1)  # code with bad count
