gi = (i for i in ())
# Test gi.gi_code.co_freevars
gi.gi_code.co_freevars
# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti
# Test gi.gi_frame.f_code.co_argcount
gi.gi_frame.f_code.co_argcount

# Test str.isidentifier()
"_".isidentifier(), "A".isidentifier(), "1".isidentifier(), "1a".isidentifier()

# Test str.isascii()
"a".isascii(), "123".isascii(), "".isascii(), "\0".isascii(), "aé".isascii()

# Test str.casefold()
"A".casefold(), "a".casefold(), "Aé".casefold(), "aé".casefold(), chr(0x10401).casefold()

# Test str.encode()
s = "abc"
s.encode()
s.encode("ascii")
s.encode("utf8")
