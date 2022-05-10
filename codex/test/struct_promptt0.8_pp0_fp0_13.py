import _struct
# Test _struct.Struct.format_parse

# CHECK: [('h', 'h', 1, True), ('i', 'i', 2, True), ('i', 'i', 2, True), ('l', 'l', 4, True)]
print(_struct.Struct('>6h').format_parse())
# CHECK: [('h', 'h', 1, True), ('i', 'i', 2, True), ('l', 'l', 4, True)]
print(_struct.Struct('>3h3i').format_parse())
# CHECK: [('i', 'i', 4, True)]
print(_struct.Struct('>2i').format_parse())
# CHECK: [('h', 'h', 2, True)]
print(_struct.Struct('>2h').format_parse())
# CHECK: []
print(_struct.Struct('').format_parse())
# CHECK: []
print(_struct.Struct('>').format_parse())
# CHECK: type=str expected
