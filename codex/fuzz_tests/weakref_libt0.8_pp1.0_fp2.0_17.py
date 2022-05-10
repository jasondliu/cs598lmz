import weakref
import sys

__all__ = ['Layer', 'Check', 'Plugin', 'Control', 'Sizer', 'Window']

class Layer(object):
    """
    """
    def __init__(self, name, options=None):
        self.name = name
        if options is None:
            options = dict(frame=False,
                           frame_color=(0,0,0,0),
                           frame_width=0,
                           frame_offset=0,
                           source=None,
                           source_color=(0,0,0,0),
                           source_width=0,
                           source_offset=0)
        self.options = options

class Check(object):
    pass

class Plugin(Layer):
    """
    """
    def __init__(self, name, options=None, order=0, states=None,
                 checks=None, playlist=None, actions=None,
                 groups=None, defaults=None, others=None):
        super(Plugin, self).__init__(name)
        self.options = options
