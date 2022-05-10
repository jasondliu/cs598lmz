import weakref
from .utils import xml_to_json, load_image
from . import _fonts


class Document(object):
    '''
    Represents an SVG document.

    Arguments:
      string: the SVG document in the form of a string.
      anchor: the anchor point where (0, 0) will be placed.
    '''

    def __init__(self, string, anchor=None):
        if anchor is None:
            self.anchor_x, self.anchor_y = 0, 0
        else:
            self.anchor_x, self.anchor_y = anchor

        self.data = xml_to_json(string)
        self.sprites = []

    def get_sprites(self):
        '''
        Get a list of all sprites in the document.
        '''
        return list(self.sprites)

    def get_sprite(self, **kwargs):
        '''
        Get a single sprite from the document.

        Arguments:
          id: the id of the sprite to get.
          xlink: the
