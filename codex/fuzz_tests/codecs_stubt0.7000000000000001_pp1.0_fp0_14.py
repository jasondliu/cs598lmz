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

print(codecs.decode("abc", "ascii", "add_one_codepoint"))
print(codecs.decode(b'abc', "utf-16", "add_utf16_bytes"))
print(codecs.decode(b'abc', "utf-32", "add_utf32_bytes"))
</code>
output
<code>abca
abab
abcdabcd
</code>
The problem with this approach is that the codec only gets one chance to recover from the error; if the codec can't fix it in one go, it gives up.  You can see that with UTF-16 decoding, as it can only add two bytes instead of four.  The closest I know of to a solution is to add a helper function that can be called repeatedly until the codec gives up.
<code>def add_utf32_bytes(exc):
    return (b'ab', exc.start+2)

def add_utf32_bytes_helper(exc):
    while exc.start &lt; len(exc.object):
        exc.start += 2
       
