import gc, weakref

from kivy.config import Config
from kivy.base import EventLoop
from kivy.factory import Factory
from kivy.graphics.texture import Texture
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.gl import gl_get_version, gl_get_vendor
from kivy.logger import Logger
from kivy.resources import resource_find
from kivy.graphics.fbo import Fbo
from kivy.graphics import RenderContext, Color, Callback, Translate, \
    Scale
from kivy.graphics.shader import Shader
from kivy.graphics.opengl import glCheckError
from kivy.graphics.transformation import Matrix

from kivy.graphics.texture import Texture
from kivy.graphics.fbo import Fbo
from kivy.graphics.vbo import Vbo
from kivy.graphics.stencil_instruct
