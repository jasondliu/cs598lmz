import codecs
# Test codecs.register_error()

import codecs

def print_unicodes(s):
    for i in range(0, len(s)):
        print "%04x" % ord(s[i]),
    print

def strict_errorhandler(err):
    print "strict:", err
    raise UnicodeDecodeError("strict", "", 0, 1, "")

def replace_errorhandler(err):
    print "replace:", err
    return ("?",)

def ignore_errorhandler(err):
    print "ignore:", err
    return ("", 0)

def xmlcharrefreplace_errorhandler(err):
    print "xmlcharrefreplace:", err
    return ("&#%d;" % ord(err.object[err.start]), err.end)

def backslashreplace_errorhandler(err):
    print "backslashreplace:", err
    return ("\\x%02x" % ord(err.object[err.start]), err.end)

def test(sample, encoding):
    print "---", encoding
    dec = codecs.get
