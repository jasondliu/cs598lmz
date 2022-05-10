import _struct

from . import gl
from . import gl_info


# create an empty struct format for the glBeginMode types
_glBeginMode_enum_formats = {}
_glBeginMode_enum_names = {}
for attr_name in dir(gl_info.GLBeginMode):
    if not attr_name.startswith('GL_'): continue
    attr = getattr(gl_info.GLBeginMode, attr_name)
    _glBeginMode_enum_names[attr] = attr_name
    _glBeginMode_enum_formats[attr] = _struct.Struct('')

# generate a format string which will be used to parse the GL data
# (this was inspired by pyglet)
def _interpret_type_size(size, type_):
    if size == 1:
        return '%s' % _glType_size_formats[type_]
    elif size == 2:
        return '%s%s' % (_glType2_size_formats[type_], _glType_size_formats[type
