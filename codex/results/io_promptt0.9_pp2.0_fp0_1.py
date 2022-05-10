import io
# Test io.RawIOBase
import _io
if not hasattr(_io, 'RawIOBase'):
    _io.RawIOBase = io.RawIOBase
    _io.BufferedIOBase = io.BufferedIOBase

# Make mimetools.Message recognize MIME "multipart/" headers when
# email.parser.BytesParser.parse() is used:
import email.parser
# The following fixes an import bug for MimeWriter.
import email.mime.multipart
import mimetools
try:
    mimetools.Message.__bases__
except AttributeError:
    mimetools.Message.__bases__ = (object, )
email.parser.Parser.feed = _Feeder(email.parser.Parser.feed)

# Fix urlparse.ParseResult._replace()
import urlparse
urlparse.ParseResult._replace = _ParseResult_replace

# Make sure all methods of http.client.HTTPConnection accept a
# context parameter as first argument.
import http.client
for method in ["request", "getresponse", "putrequest"]:
    setattr
