import codecs
# Test codecs.register_error as well as override a codec

# open file in binary bytes mode and set errors to 'ignore'
f = codecs.open(TESTFN, "rb", errors='ignore')
f.read()
f.close()

def handler_n(exc):
    return "bad\x00", 5
codecs.register_error("test.ignore", handler_n)
f = codecs.open(TESTFN, "r", errors="test.ignore")
s = f.read()
f.close()
if s != "bad" + BADBYTES[:5]:
    print("handler function ignored:", s)
    errors_found.append(1)

def handler_x(exc):
    if isinstance(exc, UnicodeDecodeError):
        print("handler got UnicodeDecodeError")
    elif isinstance(exc, UnicodeTranslateError):
        print("handler got UnicodeTranslateError")
    else:
        print("handler got other error", exc)
    return "", 2
codecs.register_error("test.replace", handler_x)
f
