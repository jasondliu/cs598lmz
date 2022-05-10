import weakref

from bravo.compat import product
from bravo.entity import Sign
from bravo.policy.mutable import DiggingPolicy
from bravo.policy.blocks import blocks, vanilla_to_beta, beta_to_vanilla
from bravo.utilities.bits import unpack_nibbles, pack_nibbles
from bravo.utilities.coords import adjust_coords_for_face
from bravo.utilities.shapes import circle_xz, rectangle_xz, scaled_circle
from bravo.utilities.shapes import line_xz, rectangle_xy, rectangle_xz

class ChunkNotLoaded(Exception):
    """
    Raised when a chunk is not loaded while it should be.
    """

class ChunkMalformed(Exception):
    """
    Raised when a chunk cannot be parsed.
    """

class Chunk(object):
    """
    A 16x16x128 block array, with block metadata, block light, and sky light.
    """

    version = (1, 4)

    __slots__ = (
