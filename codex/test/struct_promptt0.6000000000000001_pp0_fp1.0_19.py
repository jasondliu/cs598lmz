import _struct
# Test _struct.Struct with the struct module's formats.
for code in struct.__dict__:
    if code[0] == '_' or code == 'pack' or code == 'unpack':
        continue
    fmt = struct.__dict__[code]
