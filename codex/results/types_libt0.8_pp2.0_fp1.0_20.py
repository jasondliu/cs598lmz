import types
types.new_class("Image", basestring)

class Image(types.Image, object):
    """An image file path.
    
    Like a file path but is a true new_class rather than an
    old-style string subclass. This can be used to identify
    image files specifically.
    
    """

class ImageWidget(FileWidget):
    def __init__(self, *args, **kwargs):
        kwargs['base_class'] = types.Image
        kwargs['base_widget'] = Widget.get('string')
        FileWidget.__init__(self, *args, **kwargs)
