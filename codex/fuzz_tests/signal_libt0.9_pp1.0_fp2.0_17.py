import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time

try:
    import bpy
    import blf
    import mathutils
    import math
    import altus_mesh_tools as mt
except:
    pass
##
##
##
def init_blend(self):
    os.system("cls")
    sys.stderr = 0
    sys.stderr = sys.stdout
    if self.blender_started:
        return
    self.blender_started = True
    print("starting blender")

    ## Start blender with a minimal scene
    ## This allows us to draw the textures on invisible surfaces
    self.scene = bpy.data.scenes.new(name="main")
    bpy.context.screen.scene = bpy.data.scenes[self.scene.name]
    self.cam = bpy.data.cameras.new(name="cam")
    self.cam_obj = bpy.data.objects.new(self.cam.name, self
