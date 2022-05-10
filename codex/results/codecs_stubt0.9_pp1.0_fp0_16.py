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

# utf-8
print("\nutf-8")
for bad in (b'\xff', b'\xfe'):
    print("\n%r" % bad)
    for error_handler in "strict", "ignore", "replace", "add_one_codepoint":
        try:
            print("%-15s: " % error_handler, end="")
            codecs.decode(bad, "utf-8", errors=error_handler)
        except UnicodeError as exc:
            print("%s: %s" % (exc.__class__.__name__, exc))
        except Exception as exc:
            print("%s: %s" % (exc.__class__.__name__, exc))

# utf-16/32-le
print("\nutf-16-le/32-le")
for bad in (b'\xff\xfe\x00', b'\xff\xfe'):
    print("\n%r" % bad)
    for error_handler in "strict", "ignore", "replace
