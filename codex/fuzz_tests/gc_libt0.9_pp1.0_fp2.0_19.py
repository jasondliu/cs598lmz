import gc, weakref, os
import hashlib

from remotelogging import *
from time import time

#------------------------------------------------------------------------------
TEX_NUM = 0
meshes = []
actors = []
textures = []

def flush_geom():
    for m in meshes: m.flush()
    for a in actors: a.flush()
    for t in textures: t.flush()
    actors[:] = []
    meshes[:] = []
    textures[:] = []

#------------------------------------------------------------------------------
def clear_geom():
    for m in meshes: m.delete()
    for a in actors: a.delete()
    for t in textures: t.delete()
    actors[:] = []
    meshes[:] = []
    textures[:] = []

def clear_textures():
    for t in textures: gc.collect(); t.delete(); gc.collect()
    textures[:] = []

class Mesh:
    def __init__(self, g):
        self.id = 0
        self.vertices = None
        self.normals = None
        self.col
