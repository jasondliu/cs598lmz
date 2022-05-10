import codecs
# Test codecs.register_error, issue #1524.
test_support.import_module('test.test_json.test_pass2')
import test.test_json.test_pass2
j = test.test_json.test_pass2.j
codecs.register_error('strict', test.test_json.test_pass2.strict_errors)
# The error callback must not be called when encoding with ensure_ascii
# is true, because the input string is valid ASCII.
dump = j.dumps('\u20ac', ensure_ascii=True)
load = j.loads(dump)
# The error callback must be called when encoding with ensure_ascii
# is false.
dump = j.dumps('\u20ac', ensure_ascii=False)
load = j.loads(dump)
# The error callback must be called when decoding, even if the
# input is ASCII-only.
dump = j.dumps('\u20ac', ensure_ascii=True)
load = j.loads(dump, strict=True)
# Issue #1522.
