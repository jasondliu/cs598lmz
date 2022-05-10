from bz2 import BZ2Decompressor
BZ2Decompressor.__module__ = "bz2"

from _codecs import __getitem__, __doc__

if sys.version_info[0] > 2:
    import codecs
    getregentry = codecs.lookup
    def get_codec_aliases(encoding):
        codec = getregentry(encoding)
        if not codec:
            raise LookupError(encoding)

        comp_encoding = codec.compname
        base_encoding = codec.name

        aliases = [comp_encoding]
        if comp_encoding != base_encoding:
            aliases += [base_encoding]

        return aliases
else:
    getregentry = __getitem__
    def get_codec_aliases(encoding):
        aliases = []

        codec_info = []

        try:
            codec_info = __getitem__(encoding)
        except KeyError:
            codec_info = []
            if codecs.encode(codecs.decode('', encoding), encoding) == '':
                codec_info = [(
