import codecs
# Test codecs.register_error()

def bad_encoding(e):
    print("bad_encoding:", e)
    return ("\ufffd", e.start + 1)

codecs.register_error("test.lookup", bad_encoding)

for encoding in ["iso8859-1", "test.lookup"]:
    print("Encoding:", encoding)
    try:
        print(codecs.decode("\x80", encoding))
    except UnicodeError as e:
        print("ERROR:", e)
    print()
