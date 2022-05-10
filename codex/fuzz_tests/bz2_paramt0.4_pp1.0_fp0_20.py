from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2.open
from bz2 import open as bz2_open
bz2_open('somefile.bz2')

# cgi.parse_qs
from cgi import parse_qs
parse_qs('''name=foo&value=bar''')

# cgi.parse_qsl
from cgi import parse_qsl
parse_qsl('''name=foo&value=bar''')

# cgi.parse_multipart
from cgi import parse_multipart
parse_multipart('''name=foo&value=bar''')

# cgi.parse_header
from cgi import parse_header
parse_header('''name=foo&value=bar''')

# cgi.parse_multipart
from cgi import parse_multipart
parse_multipart('''name=foo&value=bar''')

# cgi.parse_multipart
from cgi import parse_multipart
parse_multipart('''name=foo&
