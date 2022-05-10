import bz2
bz2c = bz2.BZ2Compressor()
bz2d = bz2.BZ2Decompressor()

def compress(s):
    compressed = bz2c.compress(s)
    if compressed:
        return compressed
    else:
        return bz2c.flush()

def decompress(s):
    try:
        decompressed = bz2d.decompress(s)
        if decompressed:
            return decompressed
        else:
            return bz2d.flush()
    except EOFError:
        return decompressed

class MIME_Mail(MIMEBase.MIMEBase):
    def __init__(self, *args, **kws):
        MIMEBase.MIMEBase.__init__(self, *args, **kws)
        # We must call add_header, since the superclass's constructor
        # doesn't call any methods to set headers...
        self.add_header('MIME-Version', '1.0')

    def __str__(self):
        from email.Utils
