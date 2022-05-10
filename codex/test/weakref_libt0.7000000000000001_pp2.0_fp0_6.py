import weakref

from OpenGL.GL import *

from pygly.shader_program import ShaderProgram
from pygly.shader_program_builder import ShaderProgramBuilder
from pygly.texture import Texture

from . import resources


class Material( object ):

    def __init__( self ):
        super( Material, self ).__init__()

        # the program for this material
        self._program = None

        # the textures used by this material
        self._textures = {}

        # a list of property names
        self._properties = []

        # a dictionary of property names and values
        self._values = {}

    @property
    def program( self ):
        return self._program

    @property
    def textures( self ):
        return self._textures

    @property
    def properties( self ):
        return self._properties

    @property
    def values( self ):
        return self._values

    def set_program( self, program ):
        self._program = program

    def set_texture( self, name, texture ):
        self._textures[ name ] = texture
