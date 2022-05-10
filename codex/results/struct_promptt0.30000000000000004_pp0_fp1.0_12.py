import _struct
# Test _struct.Struct

# test all format characters
for fmt in _struct.__dict__.keys():
    if fmt[0] == '_' or fmt[-1] != '_':
        continue
    fmt = fmt[:-1]
    if fmt not in _struct.__dict__:
        print("missing", fmt)
    else:
        try:
            _struct.Struct(fmt)
        except ValueError:
            print("invalid", fmt)

# test all combinations of format characters
for fmt in _struct.__dict__.keys():
    if fmt[0] == '_' or fmt[-1] != '_':
        continue
    fmt = fmt[:-1]
    for fmt2 in _struct.__dict__.keys():
        if fmt2[0] == '_' or fmt2[-1] != '_':
            continue
        fmt2 = fmt2[:-1]
        try:
            _struct.Struct(fmt + fmt2)
        except ValueError:
            print("invalid", fmt + fmt2)

# test all combinations of
