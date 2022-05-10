import codecs
# Test codecs.register_error('decimal_strict', DecimalStrictError)
# Test codecs.register_error('decimal_strict_ignore_units', DecimalStrictIgnoreUnitsError)
# Test codecs.register_error('decimal_strict_ignore_units_and_sign', DecimalStrictIgnoreUnitsAndSign)

import logging
logging.basicConfig(level=logging.DEBUG)  # Log warnings and errors


def copydir(srcdir, dstdir):
    import shutil
    """Copies the contents of srcdir (relative to the current directory) to dstdir"""
    srcdir = os.path.normpath(os.path.join(os.path.curdir, srcdir))
    dstdir = os.path.normpath(os.path.join(os.path.curdir, dstdir))
    if not os.path.exists(srcdir):
        raise RuntimeError('Source directory %s not found' % srcdir)
