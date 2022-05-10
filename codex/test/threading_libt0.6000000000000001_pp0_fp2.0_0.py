import threading
threading.stack_size(67108864)

import sys
import math

import pygame

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from OpenGL.GL import shaders

VERTEX_SHADER = """
#version 130
in vec2 position;
void main()
{
    gl_Position = vec4(position, 0.0, 1.0);
}
"""

FRAGMENT_SHADER = """
#version 130
out vec4 outColor;
void main()
{
    outColor = vec4(1.0, 1.0, 1.0, 1.0);
}
"""

def compile_program():
    program = shaders.compileProgram(
        shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
        shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    )
    return program

