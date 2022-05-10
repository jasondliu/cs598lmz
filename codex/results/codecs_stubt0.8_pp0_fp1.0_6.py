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


def random_byte(size):
    if random.random() > 0.5:
        return [b"\x00", b"\xff"]
    return [bytes([random.randint(0,255)])]

# XXX: not really a random byte stream
def random_bytes(l=5, size=5):
    return [random_byte(size) for i in range(l)]

def add_errors(f, name, string, e_count, e_count2):
    def helper(processing_func):
        def wrapped(s, e):
            e_count[0] += 1
            if e_count[0] == e_count2[0]:
                e_count2[0] += 1
                return processing_func(s, e)
            else:
                raise e
        return wrapped

    for encoding in SUPPORTED_ENCODINGS:
        print("-", encoding)
        try:
            s = string.encode(encoding)
            e_count[0] = 0
            e_count2[0] = 1

           
