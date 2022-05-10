import codecs
# Test codecs.register_error('strict', codecs.strict_errors)

# Test for a bug in the unicode-escape decoder.
# This test is derived from a bug report by
# Marc-Andre Lemburg <mal@lemburg.com>.

import codecs

# This will raise a UnicodeError:
codecs.decode('\\u00fc', 'unicode-escape')

# This will raise a UnicodeError:
codecs.decode('\\u00fc', 'unicode-escape', 'strict')

# This will return a Unicode string:
codecs.decode('\\u00fc', 'unicode-escape', 'replace')

# This will return a Unicode string:
codecs.decode('\\u00fc', 'unicode-escape', 'ignore')

# This will return a Unicode string:
codecs.decode('\\u00fc', 'unicode-escape', 'xmlcharrefreplace')

# This will return a Unicode string:
