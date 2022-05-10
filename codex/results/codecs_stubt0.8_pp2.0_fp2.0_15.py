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

# Python 3 only
#with open("utf8.txt", encoding="utf-8") as f:
#    data = f.read()

with codecs.open("utf8.txt", encoding="utf-8") as f:
    data = f.read()

for n in range(1, len(data)):
    data_broken = data[:n] + data[n+1:]
    #print("Error at offset:", n)

    # UTF-8 repair strategies
    #print("\nreplace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace replace")
    #new_data = data_broken.encode("utf-8", "replace").decode("utf-8", "replace")
    #print(new_data)

    #print("\nignore i
