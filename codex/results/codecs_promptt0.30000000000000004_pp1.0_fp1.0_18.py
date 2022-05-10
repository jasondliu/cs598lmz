import codecs
# Test codecs.register_error

# This test is not exhaustive.  It only tests the error handling
# mechanism, not the actual codecs.

import codecs
import sys

def test(name):
    print "testing", name
    try:
        codecs.lookup(name)
    except LookupError, x:
        print "not found", x
        return
    try:
        u = unicode('\xff', name)
    except UnicodeError, x:
        print "can't encode", x
        return
    print "encoded", repr(u)
    try:
        u.encode(name)
    except UnicodeError, x:
        print "can't decode", x
        return
    print "decoded", repr(u)

def test_error(name):
    print "testing", name
    try:
        codecs.lookup(name)
    except LookupError, x:
        print "not found", x
        return
    try:
        u = unicode('\xff', name)
    except UnicodeError, x:
        print "can't encode",
