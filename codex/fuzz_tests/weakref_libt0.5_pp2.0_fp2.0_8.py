import weakref

import numpy as np

import pyglet

from pyglet.gl import *
import pyglet.graphics

from . import (
    gl,
    glsl,
    shader,
    texture,
    util,
)

def _get_default_shader():
    return shader.Shader(
        vertex_shader=glsl.vertex_shader,
        fragment_shader=glsl.fragment_shader,
    )

class FBO(object):
    def __init__(self, width, height, texture_format=GL_RGBA, 
                 texture_type=GL_FLOAT, texture_wrap=GL_CLAMP_TO_EDGE,
                 texture_filter=GL_LINEAR, depth_buffer=True,
                 shader=None, **kwargs):
        self.width = width
        self.height = height
        self.texture_format = texture_format
        self.texture_type = texture_type
        self.texture_wrap = texture_wrap
        self.texture_filter = texture
