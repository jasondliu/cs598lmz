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

def test_utf16_exception(encoding):
    # unicode -> encoding: exception handler is called
    handler = codecs.lookup_error("add_one_codepoint")
    u = "\ud800\udc00"
    s = codecs.encode(u, encoding, "add_one_codepoint")
    # 'a' should be inserted into the surrogate pair
    assert s == b'a\x00\x00\x00\x00'

    # encoding -> unicode: no exception handler is called
    u = codecs.decode(s, encoding, "replace")
    assert u == "a\ud800\udc00"

    # encoding -> unicode: exception handler is called
    s = b'\x00\x00\x00\x00'
    u = codecs.decode(s, encoding, "add_one_codepoint")
    assert u == "\ud800\udc00"

def test_utf32_exception(encoding):
    # unicode -> encoding: exception handler is called
   
