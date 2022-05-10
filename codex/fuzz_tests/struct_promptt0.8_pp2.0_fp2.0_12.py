import _struct
# Test _struct.Struct
# fmt:     a string
# args:    mapped to fmt string
# endian:  ">", "<", "!"
# offset:  offset in struct
# bytes:   bytes in struct
# expected: tuple for comparison
# Note:    fmt and args allow multiple offsets to be tested
props = [
    {"fmt": "b", "args": [1], "endian": ">", "offset": 0, "bytes": 1, "expected": (1,)},
    {"fmt": "b", "args": [1], "endian": "<", "offset": 0, "bytes": 1, "expected": (1,)},
    {"fmt": "b", "args": [1], "endian": ">", "offset": 1, "bytes": 2, "expected": (1,)},
    {"fmt": "b", "args": [1], "endian": "<", "offset": 1, "bytes": 2, "expected": (1,)},
    {"fmt": "b", "args": [-1], "endian": ">", "offset": 0, "bytes": 1
