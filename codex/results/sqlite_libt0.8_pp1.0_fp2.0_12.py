import ctypes
import ctypes.util
import threading
import sqlite3

import gobject
import gst

import jamendo.config as config
import jamendo.metadata as metadata
import jamendo.gstutils as gstutils


# From the mp3-extension sqlite extension
# https://github.com/jkramer/mp3-extension

tFail    = 0
tInteger = 1
tReal    = 2
tText    = 3
tBlob    = 4
tNull    = 5

# From the sqlite3 documentation.
# https://docs.python.org/2/library/sqlite3.html

PARSE_DECLTYPES = 1
PARSE_COLNAMES = 2
PARSE_COLTYPES = 3


class VorbisTagSetter(gst.Element):
    """
    This element simply sets the duration of the stream
    when it was given by the backend.
    """

    __gstdetails__ = ("Vorbis tagsetter",
                      "Generic",
                      "Set some vorbis tags",
                      "Guillaume Pellerin")

    __gstmetadata__
