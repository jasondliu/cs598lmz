import weakref

import kaa.geo
import kaa.candy
import kaa.display

class Geometry(object):
    """
    From: http://www.libsdl.org/cgi/docwiki.cgi/SDL_5fImage
    FIXME: implement all the other geometry routines (clip_rect, etc.)
    FIXME: implement all the other color routines
    """
    def __init__(self, obj):
        self.obj = weakref.ref(obj)

