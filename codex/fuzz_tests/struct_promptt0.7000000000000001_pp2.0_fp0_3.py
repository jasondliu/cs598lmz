import _struct
# Test _struct.Struct
for t in ["x", "c", "b", "B", "?", "h", "H", "i", "I", "l", "L", "q", "Q", "f", "d",
    "s", "p", "P"]:
    try:
        x = _struct.Struct(t)
    except _struct.error as e:
        print("%s: %s" % (t, e))
    else:
        print(x)

# Test _struct.pack()
for t in ["x", "c", "b", "B", "?", "h", "H", "i", "I", "l", "L", "q", "Q", "f", "d",
    "s"]:
    try:
        x = _struct.pack(t, 0)
    except _struct.error as e:
        print("%s: %s" % (t, e))
    else:
        print(x)

# Test _struct.pack_into()
for t in ["x", "c", "b", "B", "?",
