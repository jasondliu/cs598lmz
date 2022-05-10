import _struct
# Test _struct.Struct
struct = _struct.Struct('h')
struct.size
struct.pack(0)
struct.unpack(struct.pack(0))
struct.pack_into(bytearray(struct.size), 0, 0)
struct.unpack_from(struct.pack(0), 0)
struct._fmt
struct._fmt_chars
struct._fmt_re
struct._fmt_is_native
struct._fmt_is_standard
struct._fmt_is_native
struct._fmt_is_standard
struct._fmt_is_native
struct._fmt_is_standard
struct._fmt_is_native
struct._fmt_is_standard
struct._fmt_is_native
struct._fmt_is_standard
struct._fmt_is_native
struct._fmt_is_standard
struct._fmt_is_native
struct._fmt_is_standard
struct._fmt_is_native
struct._fmt_is_standard
struct._fmt_is_native
struct._fmt_is_standard
struct._fmt
