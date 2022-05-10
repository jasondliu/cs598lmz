import codecs
codecs.register_error('strict', codecs.ignore_errors)

# ---------------------------------------------------------------------

class PdfFileReader(object):
    """
    This class supports reading PDF files.
    """
    def __init__(self, stream, strict=True, warndest=None, overwriteWarnings=True):
        """
        Initializes the PdfFileReader object.

        stream is a file object (usually a text one) from which the
        input PDF will be read.  You can not close the file object
        until you have completely read the file.  This is because
        portions of the PDF file may still be sitting in a buffer.

        strict is an optional parameter.  When False, PDF files
        that don't follow the PDF standard will still be parsed.
        Otherwise, these files will cause an PdfReadError to be
        raised.

        warndest is an optional parameter.  If present, it should be
        a file-like object to which all warnings will be written.
        Otherwise, the warnings will be ignored.

        overwriteWarnings is an optional parameter. If True (the default),
        any previously registered warning
