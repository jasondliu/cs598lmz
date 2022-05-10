import weakref

from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.label import Label

from components.graphic import Graphic
from components.physics import Physics
from components.position import Position
from components.renderable import Renderable

class TextRenderable(Renderable):
    def __init__(self, *args, **kwargs):
        super(TextRenderable, self).__init__(*args, **kwargs)
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)
        self.font_size = kwargs.get('font_size', 12)
        self.text = kwargs.get('text', '')
        self.color = kwargs.get('color', [0, 0, 0, 1])

    def render(self, position, physics, graphic):
        self.label.text = self.text
        self.label.texture_update()
        self.label.pos = position.x, position.y
       
