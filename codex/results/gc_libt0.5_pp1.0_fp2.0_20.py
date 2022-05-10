import gc, weakref
import sys
import pygame
import pygame.locals
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.arrays import vbo
from OpenGL.GL import shaders
from OpenGL.GL.ARB.vertex_array_object import glGenVertexArrays, glBindVertexArray
from OpenGL.GL.shaders import compileShader, compileProgram
from numpy import array, float32
from numpy.random import random
import numpy as np

from OpenGL.GL.shaders import *
from OpenGL.GL.ARB.vertex_shader import *
from OpenGL.GL.ARB.fragment_shader import *
from OpenGL.GL.ARB.geometry_shader4 import *

from OpenGL.GL.ARB.tessellation_shader import *
from OpenGL.GL.ARB.compute_shader import *
from OpenGL.GL.ARB.shading_language_include import *

from OpenGL.GL.ARB.vertex_type_2_10_10_10
