import _struct
import _utils
import _vars

#-------------------------------------------------------------------------------
def _get_struct_name(s):
    return s.__name__

#-------------------------------------------------------------------------------
def _get_struct_fields(s):
    return s._fields_

#-------------------------------------------------------------------------------
def _get_struct_field_names(s):
    return [f[0] for f in s._fields_]

#-------------------------------------------------------------------------------
def _get_struct_field_types(s):
    return [f[1] for f in s._fields_]

#-------------------------------------------------------------------------------
def _get_struct_field_type(s, name):
    return [f[1] for f in s._fields_ if f[0] == name][0]

#-------------------------------------------------------------------------------
def _get_struct_field_offset(s, name):
    return [f[1] for f in s._fields_ if f[0] == name][0]

#-------------------------------------------------------------------------------
def _get_struct_field_size(s, name):
    return _struct.calcsize(_get_struct_field_type(s, name
