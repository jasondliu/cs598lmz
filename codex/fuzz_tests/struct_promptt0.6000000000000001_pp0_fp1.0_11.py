import _struct
# Test _struct.Struct()

# _struct.Struct()
with raises(TypeError):
    _struct.Struct()

# _struct.Struct(0)
with raises(TypeError):
    _struct.Struct(0)

# _struct.Struct('x')
with raises(TypeError):
    _struct.Struct('x')

# _struct.Struct(' x')
with raises(TypeError):
    _struct.Struct(' x')

# _struct.Struct('1')
with raises(TypeError):
    _struct.Struct('1')

# _struct.Struct('1x')
with raises(TypeError):
    _struct.Struct('1x')

# _struct.Struct('1p')
with raises(TypeError):
    _struct.Struct('1p')

# _struct.Struct('1s')
with raises(TypeError):
    _struct.Struct('1s')

# _struct.Struct('1c')
with raises(TypeError):
    _struct.Struct('1c')

# _struct.Struct('1b')
with raises(TypeError
