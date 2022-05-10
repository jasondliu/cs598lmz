import codecs
# Test codecs.register_error, with unicode containing surrogates,
# and with backslashreplace.
class MyError(UnicodeError):
    def __init__(self, encoding, msg, object, start, end, reason):
        UnicodeError.__init__(self, encoding, msg, object, start, end)
        self.reason = reason

    def __str__(self):
        return '%s (reason: %s)' % (UnicodeError.__str__(self), self.reason)

def my_handler(error):
    reason = {1: 'stray lead surrogate',
              2: 'unexpected end of data',
      3: 'missing low surrogate',
              }
    raise MyError(error.encoding, error.reason,
                  error.object, error.start, error.end,
                  reason[error.reason])

# Input: UTF-16 encoding w/o BOM,
# with lead surrogate missing in even position,
# with stray lead surrogate in odd position
# and missing low surrogate as last character
