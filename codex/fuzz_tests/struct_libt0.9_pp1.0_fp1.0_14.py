import _struct
import matplotlib.image
import requests
from io import BytesIO
import numpy
from struct import unpack_from
import re

def get_image(typ=None,source=None,name=None,url=None,path=None,telescope=None,instrument=None,reference=None):
    """This function will try to get an <Image> object.

    It will try to deal with a range of inputs and figure out exactly what is requested.

    ..note::

    -- This function currently assumes that the source is 'imageserver'.
    -- The source will be implemented later, and this function will then query many different source types.

    :param typ: str. This can be 'fits' or 'jpeg'. Other options will be implemented later.
    :param source: str. This will typically be 'imageserver'. Other options may be added in future.
    :param name: str. This is the name of the image. This can either be the actual name of a file on the imageserver, or the REST url (which should be intelligable to the imageserver).
    :param url: str. This
