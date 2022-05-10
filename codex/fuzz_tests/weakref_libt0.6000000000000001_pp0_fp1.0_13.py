import weakref
import traceback

import bpy

from . import exceptions
from . import util

class OperatorProperties(bpy.types.PropertyGroup):
    '''
    This is a magic class that is used to store properties for each operator
    '''
    pass

class Operator(bpy.types.Operator):
    bl_idname = "scene_update.operator"
    bl_label = "Scene Update"
    bl_description = "Scene Update"
    bl_options = {'REGISTER', 'UNDO'}

    def __init__(self):
        self.watched_props = []
        self.is_executing = False
        self.is_modal_running = False
        self.is_undo_registered = False
        self.is_redo_registered = False
        self.value_history = {}
        self.error_message = None
        self.props = None
        self.__class__.bl_rna = bpy.types.SceneUpdate.bl_rna
        self.__class__.properties_class = OperatorProperties
