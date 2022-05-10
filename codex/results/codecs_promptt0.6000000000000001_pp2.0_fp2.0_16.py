import codecs
# Test codecs.register_error()
def hex_unescape_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = exc.object[exc.start:exc.end]
        if len(s) == 2 and s[0] == '\\' and '0' <= s[1] <= '9':
            return (chr(int(s[1])), exc.end)
        if len(s) == 3 and s[0] == '\\' and s[1] == 'x' and '0' <= s[2] <= '9':
            return (chr(int(s[2], 16)), exc.end)
        if len(s) == 4 and s[0] == '\\' and s[1] == 'u' and '0' <= s[2] <= '9':
            return (chr(int(s[2:], 16)), exc.end)
        if len(s) == 6 and s[0] == '\\' and s[1] == 'U' and '0' <= s[2] <= '9':
            return (chr
