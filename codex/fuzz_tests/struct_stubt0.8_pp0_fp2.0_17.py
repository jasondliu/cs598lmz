from _struct import Struct
s = Struct.__new__(Struct)

raw_bytes = s.pack("b", 123)

print("Raw bytes: {}".format(raw_bytes))
print("Raw bytes as ASCII: {!r}".format(raw_bytes.decode("ascii")))

# binascii
# http://docs.python.org/3.4/library/binascii.html
# Модуль, позволяющий преобразовывать строки в бинарный вид и наоборот
import binascii

def to_hex(t, nbytes):
    """Преобразует в шестнадцатеричную строку без пропуска нулей."""
    h = hex((
