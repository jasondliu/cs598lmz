import codecs
# Test codecs.register_error with test_pyio.
# Issue #17953: Verify that errors are reported only for code points above
# 0x10ffff.
for name in ('ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace', 'xmlcharrefreplace'):
    encoder = codecs.getincrementalencoder('utf-16le')(name)
    encoder.encode(u'\ue000')
