import weakref

import pyglet
from pyglet.graphics import Batch

from . import util
from . import batched
from . import graphics


def link_attrs(group=None, attrs=None, base=None, prefix=None, suffix=None):
    """
    link the attributes of a group to those of another group.
    """
    if prefix is None:
        prefix = ''
    if suffix is None:
        suffix = ''
    if base is None:
        base = group
    if attrs is None:
        attrs = [
            'x', 'y', 'z',
            'batch',
            'visible', 'opacity',
            'rotation',
            'rotation_center',
            'scale',
            'scale_center',
            'anchor_x', 'anchor_y',
        ]

    attrs = [a for a in attrs if hasattr(group, a)]

    for attr in attrs:
        attr_name = '{}{}{}'.format(prefix, attr, suffix)
