from lzma import LZMADecompressor
LZMADecompressor.__doc__ = """
LZMA Decompressor for xz- or lzma-compressed data.

:param format:
    The format of the input data. The default format is ``lzma``, which is
    compatible with both xz- and lzma-compressed data.

:param filters:
    List of dicts that specify the filter chain for the new compressor.
    This can be used to select a different compression level or disable
    the integrity check for the stream.

    If no filters are given, the format's default filter chain is used.

    The list should contain dicts with following keys:

    id
        ID of the filter. Currently supported: ``FILTER_LZMA1``.

    preset
        Compression level. This is an integer from 0 to 9, inclusive.
        1 is fastest and produces the least compression,
        9 is slowest and produces the most compression.
        0 means that the preset is read from the stream.

    If a preset is given for a filter, it overrides the preset for
    the whole stream.

"""


class LZMAComp
