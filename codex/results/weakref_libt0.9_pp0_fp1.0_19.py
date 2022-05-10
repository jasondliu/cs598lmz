import weakref

import kaa
import kaa.notifier
import kaa.display
import kaa.input
import kaa.cui
import kaa.geometry
import kaa.keys
import kaa.evlist

if sys.version_info >= (3, 0):
    def ascii_ord(c):
        return ord(c)
else:
    def ascii_ord(c):
        if isinstance(c, str):
            return ord(str(c))
        else:
            return c


class Theme(object):

    def __init__(self, palettedef, text_style=None, layout_style=None,
                 layout_style_cont=None, layout_style_sel=None, layout_style_cur=None,
                 keydef=None, keydef_textmark=None, keydef_list=None, keydef_textlist=None,
                 document_style=None, screen_style=None, screen_margin=None,
                 screen_max_frame=None,
                 cursor_visible=True, cursor_shape=
