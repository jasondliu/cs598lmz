import _struct
# Test _struct.Struct.__sizeof__
print('sizeof(Struct()) =>', _struct.Struct().__sizeof__())
print('sizeof(Struct("i")) =>', _struct.Struct("i").__sizeof__())
print('sizeof(Struct("ii")) =>', _struct.Struct("ii").__sizeof__())
print('sizeof(Struct("iih")) =>', _struct.Struct("iih").__sizeof__())
print('sizeof(Struct("iih", True)) =>', _struct.Struct("iih", True).__sizeof__())
print('sizeof(Struct("iih", False)) =>', _struct.Struct("iih", False).__sizeof__())
