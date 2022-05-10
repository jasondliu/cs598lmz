import codecs
# Test codecs.register_error()

import codecs
import sys

# Codecs which use 'replace' as default error handler
for encoding in ['ascii', 'latin-1', 'iso8859-1']:
    if encoding in codecs.aliases.aliases:
        continue
    # register a new error handler with a new name
    codecs.register_error(encoding + '-replace', codecs.replace_errors)
    # encode and decode a string
    s = '\xe4\xf6\xfc\xdf'
    try:
        encoded = s.encode(encoding)
    except LookupError:
        continue
    decoded = encoded.decode(encoding + '-replace')
    # now check the result
    if s != decoded:
        print("Error with encoding", encoding)
        sys.exit(1)

# Codecs which use 'ignore' as default error handler
for encoding in ['ascii', 'latin-1', 'iso8859-1']:
    if encoding in codecs.aliases.aliases:
        continue

