import ctypes
import ctypes.util
import threading
import sqlite3
import contextlib
import os
import sys

import numpy as np

import bpy

################################################################################
# Blender utility functions to access objects, meshes and materials
################################################################################

def get_mesh(obj):
    """Get access to the Mesh data from a Blender object.
    Returns None if the object has no mesh data."""
    if obj.type != 'MESH':
        return None
    return obj.data

def get_materials(obj):
    """Gets the materials from a Blender Mesh.
    Returns an empty list if the object has no materials."""
    mesh = get_mesh(obj)
    if mesh is None:
        return []

    material_slots = mesh.material_slots
    return [slot.material for slot in material_slots if slot.material is not None]

def get_material_name(material):
    """Gets the material name, falling back to the first texture used by the
    material if it has no name."""
    if material.name is not None:
        return material.name

    for
