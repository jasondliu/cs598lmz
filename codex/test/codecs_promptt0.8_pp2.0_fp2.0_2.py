import codecs
# Test codecs.register_error:
#  - use unencodable character to trigger the registered codec error
#  - use long string to trigger the internal buffer overflow error
#  - verify that the callback argument is processed correctly
#
for buffer_overflow in ('ignore', 'replace', 'surrogateescape'):
    for character in (b'A', b'\xff'):
        for callback in (lambda e: (b'?', e.start + 1), lambda e: (b'?', 1)):
            def codec(encoding):
                return codecs.lookup(encoding).encode(character * 10,
                    errors=buffer_overflow)
