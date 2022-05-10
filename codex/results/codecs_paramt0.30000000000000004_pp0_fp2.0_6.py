import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_encoding(file):
    """
    Returns the encoding of a file.
    """
    # First try to get encoding from a BOM
    with open(file, 'rb') as f:
        raw = f.read(4)
    for enc,boms in \
        ('utf-8-sig',(codecs.BOM_UTF8,)),\
        ('utf-16',(codecs.BOM_UTF16_LE,codecs.BOM_UTF16_BE)),\
        ('utf-32',(codecs.BOM_UTF32_LE,codecs.BOM_UTF32_BE)):
        if any(raw.startswith(bom) for bom in boms):
            return enc
    # Next try to get encoding from the locale
    try:
        import locale
        enc = locale.getpreferredencoding()
        # On Windows, CP1252 is sometimes returned, which is actually
        # a superset of latin-1.
        if
