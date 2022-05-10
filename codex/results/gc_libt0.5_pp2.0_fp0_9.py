import gc, weakref
from weakref import WeakValueDictionary

import numpy as np

from OpenGL.GL import GL_RGBA, GL_UNSIGNED_BYTE, GL_TEXTURE_2D, GL_LINEAR, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER, GL_NEAREST, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_REPEAT, GL_CLAMP_TO_EDGE
from OpenGL.GL import glGenTextures, glDeleteTextures, glBindTexture, glTexImage2D, glTexParameteri, glTexSubImage2D

from kivy.graphics.texture import Texture
from kivy.graphics.texture import TextureRegion
from kivy.graphics.opengl_utils import gl_get_default_framebuffer, gl_info
from kivy.graphics import fbo
from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.logger import Logger

from kivy.graphics.transformation import Matrix

from kivy
