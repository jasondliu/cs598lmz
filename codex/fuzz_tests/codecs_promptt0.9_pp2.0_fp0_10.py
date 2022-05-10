import codecs
# Test codecs.register_error(decoder)
# Make sure that the implicit utf-8 codec can be used with
# error handler.

codecs.register_error("custom", codecs.ignore_errors)
try:
    u = 'R\xe4\xfcdiger'
    u.encode("cp037", "custom")
    if unichr(150) != u'\xe4':
        raise test_support.TestFailed("unichr returned wrong value for latin1")
    u = u'R\xe4diger'
    u.encode("utf-8", "custom")
    if unichr(150) != u'\xe4':
        raise test_support.TestFailed("unichr returned wrong value for latin1")
    u.encode("latin-1", "custom")
    u = unichr(sys.maxunicode)
    u.encode("utf-8", "custom")
except LookupError:
    raise test_support.TestFailed, "can't encode character"

def test_bug_390791():
