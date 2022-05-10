import _struct
# Test _struct.Struct and its methods.

struct_tests = [
    # normal formats
    ('b', ['0', '0'], _struct.error),
    ('b', ['1', '1'], '\x01'),
    ('b', ['10', '1'], '\n'),
    ('b', ['127', '1'], '\x7f'),
    ('b', ['-1', '0'], _struct.error),
    ('b', ['-2', '1'], _struct.error),
    ('b', ['-10', '1'], _struct.error),
    ('b', ['-20', '1'], _struct.error),
    ('b', ['-128', '1'], '\x80'),
    ('B', ['0', '1'], '\x00'),
    ('B', ['1', '1'], '\x01'),
    ('B', ['10', '1'], '\n'),
    ('B', ['127', '1'], '\x7f'),
    ('B', ['128', '0'], '\
