import codecs
codecs.register_error("mixed-ignore", codecs.ignore_errors)

def make_text_stream(filename, errors="strict"):
    """
    Creates a text stream from a file.
    
    This is basically a proxy for codecs.open() with a few niceties for
    dealing with manifest files. It will first look for a UTF-8-encoded
    file with BOM and use that if it exists. If there is no UTF-8-encoded
    file with BOM, it will look for an ISO-8859-1-encoded file and convert
    that to UTF-8.
    """
    utf8_bom_file = filename + ".utf8-bom"
    if os.path.exists(utf8_bom_file):
        return codecs.open(utf8_bom_file, encoding="utf-8-sig",
                           errors=errors)
    utf8_file = filename + ".utf8"
    if os.path.exists(utf8_file):
        return codecs.open(utf8_file, encoding="
