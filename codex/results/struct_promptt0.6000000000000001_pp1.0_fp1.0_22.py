import _struct
# Test _struct.Struct.
_struct.Struct(">I").pack(1)
# Test _struct.Struct.__len__
len(_struct.Struct(">I"))
# Test _struct.Struct.format
_struct.Struct(">I").format
# Test _struct.Struct.size
_struct.Struct(">I").size
# Test _struct.Struct.unpack
_struct.Struct(">I").unpack(_struct.Struct(">I").pack(1))

import _symtable
# Test _symtable.symtable
_symtable.symtable("def f(): pass", "<test>", "exec")
_symtable.symtable("def f(): pass", "<test>", "exec", optimize=0)
# Test _symtable.symtable.__len__
len(_symtable.symtable("def f(): pass", "<test>", "exec"))
# Test _symtable.symtable.get_symbols
_symtable.symtable("def f(): pass", "<test>", "exec").get_symbols()
# Test _symtable.symtable.get_lines
_sym
