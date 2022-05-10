import _struct
# Test _struct.Struct.__repr__
print("repr(s)", repr(s))
# Test alignment
try:
    _struct.Struct("<HI")
except (TypeError, _struct.error) as e:
    print("TypeError:", e)
try:
    _struct.Struct("<HI5s")
except (TypeError, _struct.error) as e:
    print("TypeError:", e)
# Test endianness
try:
    _struct.Struct("=")
except (TypeError, _struct.error) as e:
    print("TypeError:", e)
for c in "<@=!<>":
    try:
        _struct.Struct(c)
    except (TypeError, _struct.error) as e:
        print("TypeError:", e)
x = "12345678"
s = _struct.Struct("=HHH8s")
pad = (calcsize("HHH") - calcsize("8s")) * '\0'
print("pad:", repr(pad))
print("H*", [h * 256 + l
