import weakref
import skimage.draw

class LineMode:
    SINGLE=(0,'single')
    DOUBLE=(1,'double')
    
    def __init__(self, id, name):
        self.id=id
        self.name=name
        
    @property
    def is_single(self):
        return self.id==0

    @classmethod
    def _choices(cls):
        return [ (e.id, e.name) for e in [LineMode.SINGLE, LineMode.DOUBLE] ]
    
class RichLine:
    def __init__(self, scale=0, diameter=0.0, color=(1,0,0), layer=0, line_mode=LineMode.SINGLE, id=0, line_fallback=0.0):
        if isinstance(color, skimage.color.ColorSpace):
            color = color.rgba[0:3]
        self.scale=scale
        self.diameter=diameter
        self.id=id
        self.color=color
        self
