import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

# For internal use only.
def _bootstrap():
    try:
        import _codecs_cn, _codecs_hk, _codecs_iso2022, _codecs_jp, _codecs_kr, _codecs_tw, _multibytecodec
        if sys.maxunicode > 65535:
            import _codecs_jp_o11r, _codecs_jp_o16r, _codecs_kr_o16r, _codecs_tw_o16r, _codecs_tw_surrogate
    except ImportError as msg:
        if not hasattr(sys, "pypy_version_info"):
            print(msg)
        return

if __name__ == '__main__':
    _bootstrap()
