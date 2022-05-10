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

encoding_name = sys.argv[1]
extra_bytes = int(sys.argv[2])
raise_exception = sys.argv[3] == 'true'

# Note: we use raw-unicode-escape below to avoid a crash in 2.6.9 on OSX
# when we decode with utf-32. See #10265.
input_text = u'\u0080\n'.encode('raw-unicode-escape').decode(encoding_name)
tokens = u'test\n'

input_text += tokens[:extra_bytes]

output_text = tokens[extra_bytes:] + u'a\n'

# Uncomment this to see non-Python version compare output
#print('input:')
#print(input_text)
#print('output:')
#print(output_text)

if encoding_name.startswith('utf-32'):
    c = codecs.iterdecode(io.StringIO(input_text), encoding_name, 'add_utf32_bytes')
