import codecs
# Test codecs.register_error() function
def bad_ones(exc):
    if isinstance(exc, codecs.UnicodeDecodeError):
        start = exc.start
        end = exc.end
        if start == 0: return u"\uFFFD" * (end - start)
        # bad characters in the middle are replaced by spaces
        return " " * (end - start)
    elif isinstance(exc, codecs.UnicodeEncodeError):
        # Output "replacement", if you want to
        replacement = u"\ufffd"*len(exc.object[exc.start:exc.end])
        # Or output the exception
        # replacement = str(exc)
        return (replacement, exc.end)
    else: return None
codecs.register_error("test.bad_ones", bad_ones)
