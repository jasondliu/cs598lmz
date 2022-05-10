import _struct
# Test _struct.Struct
assert(isinstance(_struct.Struct('i'), _struct.Struct))
assert(isinstance(_struct.Struct('i', True), _struct.Struct))
assert(isinstance(_struct.Struct('i', False), _struct.Struct))
assert(isinstance(_struct.Struct('i', True, True), _struct.Struct))
assert(isinstance(_struct.Struct('i', True, False), _struct.Struct))
assert(isinstance(_struct.Struct('i', False, True), _struct.Struct))
assert(isinstance(_struct.Struct('i', False, False), _struct.Struct))
assert(isinstance(_struct.Struct('i', True, True, True), _struct.Struct))
assert(isinstance(_struct.Struct('i', True, True, False), _struct.Struct))
assert(isinstance(_struct.Struct('i', True, False, True), _struct.Struct))
assert(isinstance(_struct.Struct('i', True, False, False), _struct.Struct))
assert(isinstance(_struct.Struct('i', False, True, True), _struct.Struct))
