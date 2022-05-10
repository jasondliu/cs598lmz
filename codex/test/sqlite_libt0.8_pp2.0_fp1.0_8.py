import ctypes
import ctypes.util
import threading
import sqlite3
import os

from ufo2ft.kern import KernReader, KernTable


def get_libfreetype():
    """Return freetype library object."""
    pathname = ctypes.util.find_library("freetype")
    try:
        return ctypes.CDLL(pathname)
    except OSError as e:
        raise RuntimeError("Failed to load FreeType library: %s" % e)


class KernTableBuilder(object):

    def __init__(self, ft_lib):
        self.ft_lib = ft_lib

    def build(self, font_filepath):
        ft_face_p = self._get_ft_face(font_filepath)
        try:
            ft_face = ft_face_p.contents
            kern_table = self._get_kern_table(ft_face)
        finally:
            self.ft_lib.FT_Done_Face(ft_face_p)
        return kern_table

