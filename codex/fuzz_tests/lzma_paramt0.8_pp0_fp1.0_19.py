from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor

from pyx.canvas import canvas
from pyx import color, path, text, unit


# Make sure that PyX is working with the same version of color as we are.
if color.cmyk_color.version != color.version:
    raise ImportError("color version mismatch")


# A couple of color names are changed with respect to SVG. First, we
# need to be able to translate from the SVG names to the less
# consistent ones used by PyX.
color_name_translation_table = {
    "indigo": "violet",
    "darkviolet": "violetred",
    "darkgrey": "gray40",
    "goldenrod": "gold",
    "mediumpurple": "purple",
    "mediumvioletred": "violetred",
    "darkcyan": "cyan",
    "mediumslateblue": "slateblue",
    "darkorchid": "orchid",
    "darkslateblue": "slateblue",
    "darkslategray": "slategray",
