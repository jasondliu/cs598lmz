from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = __patched_decompress

from html import unescape

from urllib.parse import urlparse, urlunparse, quote, unquote, urlencode, parse_qsl
EscapeVars = quote
UnescapeVars = unquote
from urllib.request import urlopen
from novalabs.core.ipaddress import IP4Address


class TMessageWriter(object):
    response_wd = {200: 'OK'}
    line_ending = '\r\n'.encode()
    encoding = 'utf8'

    def __init__(self, o_file, request=None, script_name='', keep_connection_open=False):
        # type: (Any, TRequest, Union[str, bytes], bool) -> None
        # kill the old line_ending, resulting from a previous output:
        old_o_file_len = len(o_file.getvalue())
        if old_o_file_len > 0 and not (
                o_file.getvalue()[-2:] == self.line_ending or
               
