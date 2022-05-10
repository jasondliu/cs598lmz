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
