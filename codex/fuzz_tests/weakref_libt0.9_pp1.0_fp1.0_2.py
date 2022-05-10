import weakref
import shutil
from os import stat
from csv import QUOTE_MINIMAL
from svg.etree import stringify
from svg.svgelements import Path
from statengine.client import get_stat
from core import *
from utils import *
from storage import storage, storage_factory
from path import path


class Album(object):
    """The sole purpose of this class is to model the container for images,
       to be rendered, pretty much like a photographs album, thus the name
       for this class.

       The initalization of the class gets a number of arguments, the 
       directory of the images, the destination of the rendered image and
       template, the name of the game and a set of parameters that control
       the creation of the html file in the process of creating the 
       SVG image.

       After initialization and calling of the "load" method, it would be
       possible to access a set of attributes for this class, including
       the title, the photos, and the album itself.

    """

    _cached_albums = weakref.WeakValueDictionary()
    cache
