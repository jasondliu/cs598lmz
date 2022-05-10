import _struct
# Test _struct.Struct().pack_into()'s packed chunk size against a manual estimate.
# The latter is taken from the _struct docs and a supplementary comment on:
# https://bugs.python.org/issue16406

chunk_size = 0
for fmt, expected in (
        ('i', 4),
        ('gf', 16),
        ('fd', 16),
        ('dd', 16),
        ('qq', 32),
        ('QQ', 32),
    ):
    format_obj = _struct.Struct(fmt)
    chunk_size = max(chunk_size, format_obj.size)
    chunk_size += (-chunk_size) % format_obj.alignment
    assert chunk_size == expected, (fmt, chunk_size, expected)
