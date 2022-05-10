import _struct
# Test _struct.Struct
t = _struct.Struct('i')
for f in ['i', 'l', 'h', 'q', 'i', 'l', 'h', 'q', 'i', 'l', 'h',
'q', 'i', 'l', 'q', 'f', 'd', 'P', 'P', 'P']:
  try:
    t = _struct.Struct(f)
  except ValueError as e:
    print("""Expected error: %s -- repr value: %r -- should be %r""" %
          (e, e, ValueError("bad char for struct fmt: '%s' \"expected '@' or '='
          or '<' or '>' or '!'\"" % f)))
  except Exception:
    print("Unexpected error")

# memory check
t = _struct.Struct('i')
print(t)
print(repr(t))
print(t.size)
print(t.format)
try:
  t.pack(1, 2)
except TypeError:
  print("""Expected TypeError exception""")


