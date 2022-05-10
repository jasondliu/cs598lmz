import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

datas = [
    b"",
    b"caf\xe9" + os.urandom(20),

    # Padding with an overlong UTF-8 sequence that takes two chars and
    # is longer than the UCS1 representation of the character encoded.
    b"caf\xfc\x80\x80" + os.urandom(20),
]

for enc in "utf-8", "utf-16-le", "utf-32-le":
    for data in datas:
        print(enc, data)

        for errors in "strict", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes":

            # Unicode decode error on data
            try:
                data.decode(enc, errors)
            except UnicodeDecodeError as exc:
                print("  UnicodeDecodeError:", exc)
                assert exc.object is data

            # Unicode encode error on encoded data
            try:
                data.decode(enc).encode(enc, errors)
            except UnicodeEncodeError as exc:

