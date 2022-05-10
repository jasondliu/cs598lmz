import ctypes
# Test ctypes.CField
################################################################################
# CField
class CField(ctypes.Structure):
	_fields_ = [
		("name", ctypes.c_char_p),
		("type", ctypes.c_char_p),
		("required", ctypes.c_int),
		("size", ctypes.c_int),
		("offset", ctypes.c_int),
	]

# CFieldList
class CFieldList(ctypes.Structure):
	_fields_ = [
		("size", ctypes.c_int),
		("data", ctypes.POINTER(CField)),
	]

# Test
field_name = "test_name"
field_type = "test_type"
field_required = 2
field_size = 4
field_offset = 6

field = CField()
field.name = field_name
field.type = field_type
field.required = field_required
field.size = field_size
field.offset = field_offset

field_list = CFieldList()
field_
