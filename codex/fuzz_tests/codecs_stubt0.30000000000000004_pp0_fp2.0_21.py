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

# Test the codecs module

import codecs
import sys

def test(encoding, testcases):
    print("Trying encoding %s" % encoding)
    for i in range(len(testcases)):
        testcase = testcases[i]
        print("Testcase %d" % i)
        print("in:", testcase[0])
        print("out:", testcase[1])
        print("encoding:", end=' ')
        try:
            x = testcase[0].encode(encoding)
            print(repr(x))
            if x != testcase[1]:
                print("Encoding of %s to %s is %s, should be %s" %
                      (repr(testcase[0]), encoding, repr(x), repr(testcase[1])))
        except UnicodeError as reason:
            print("ERROR", reason)
        print("decoding:", end=' ')
        try:
            x = testcase[1].decode(encoding)
            print(repr(x))
            if
