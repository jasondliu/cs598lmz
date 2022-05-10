import weakref
import warnings
from math import (cos, sin, pi, sqrt)

from . import chasles, rpy

from . import cgtypes
from . import cgmath
from . import engine

__all__ = [
    'vec3', 'vec4', 'quat', 'mat3', 'mat4', 'hmat',
    'set_default_engine_name', 'set_default_engine',
    'distance', 'lerp', 'slerp', 'angle', 'cross', 'dot', 'normalized',
    'interpolate_cubic', 'interpolate_hermite',
    'BaseEngine', 'NotImplementedEngine',
    ]


def set_default_engine_name(name):
    """Set the name of the default engine.
    
    'name' is the name of the engine.
    
    """
    if name not in engine.engines_by_name:
        raise KeyError(
            "cgmathpy: unknown engine '%s'" % name)
    engine.default_engine = engine.engines_
