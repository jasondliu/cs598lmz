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

    def _get_obj(self):
        obj = self.obj()
        if not obj:
            raise ReferenceError, "parent has been deleted"
        return obj

    def _get_surface(self):
        obj = self._get_obj()
        if isinstance(obj, kaa.Surface):
            return obj
        raise TypeError, "obj is not a surface"

    def __getattr__(self, attr):
        if attr in ('width', 'height'):
            obj = self._get_obj()
            return getattr(obj.geometry, attr
