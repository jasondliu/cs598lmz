import threading
threading.Thread._thread_started = False

import PIL.Image

from . import config, event, rasterize, render
from .render import renderer_dict
from .geo import geo_to_float, geo_to_int, geo_to_pixel, Pixel
from .layers import layer_dict
from .tileio import tile_io_handler, TileIterator

log = logging.getLogger('tilestache')


def clean_path (path):
    """ Get rid of any leading/trailing slash, plus any embedded double-slashes.
    """
    path = re.sub('/+', '/', path)
    path = path.strip('/')
    return path


class Config:
    """ TileStache config object.
    """
    class Error(Exception):
        pass

    def __init__ (self, filepath):
        """ Load configuration from a JSON file.
        """
        self.layers = config.buildConfiguration(filepath)


class Request:
    """ Object for holding information about a single request.
    """
    def __init__ (
