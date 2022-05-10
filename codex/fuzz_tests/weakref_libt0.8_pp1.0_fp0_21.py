import weakref

from kivy.app import App
from kivy.graphics import (
    Color, Rectangle, Line, Ellipse, Triangle,
    Quad, Mesh, Bezier, RoundedRectangle,
    BindTexture)
from kivy.graphics import (
    PushMatrix, PopMatrix, Translate, Scale, Rotate,
    Mesh, Fbo, ClearColor, ClearBuffers, ScaleTo,
    Scale)
from kivy.graphics import PushState, PopState
from kivy.graphics.opengl import glReadPixels, gl_utils
from kivy.lang import Builder
from kivy.properties import (
    ObjectProperty, ListProperty, NumericProperty,
    BooleanProperty, OptionProperty, AliasProperty)
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.vector import Vector

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton

KV = """
<
