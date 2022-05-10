from lzma import LZMADecompressor
LZMADecompressor()
from re import findall
from subprocess import PIPE
from subprocess import Popen
from sys import stderr
from sys import stdin
from sys import stdout
from tarfile import TarFile
from tarfile import TarInfo
from time import time
from zlib import decompress
from zlib import MAX_WBITS


def main():
    on_call_exception = False
    try:
        call_main(sys.argv)
    except dulwich.errors.GitProtocolError as e:
        if on_call_exception:
            raise
        on_call_exception = True
        remote_name, remote_location = sys.argv[-2:]
        if e.args and e.args[0].startswith('expected old/new/ref, got'):
            url_type = 'ssh'
            user_host, path = remote_location.split(':', 1)
            canonical_host = None
            for host in gethostbyname_ex(user_host)[2]:
                if host == user_host:
                    continue
