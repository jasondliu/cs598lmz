import _struct
print(max(_struct.unpack(">f", _struct.pack(">f", 1e+50))))  # works
print(max(_struct.unpack(">d", _struct.pack(">d", 1e+300))))  # works
print(max(float(1e+300), "float"))  # does not work (infinite loop)
