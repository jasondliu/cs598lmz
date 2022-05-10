import gc, weakref

import render_mesh_draw as Draw

import pyfbsdk_additions
from pyfbsdk_additions import *

import render_tools as rTools

import ri

class sceneRenderer(object):
    def __init__(self):
        AnimationTool().OnUIIdle.Add(self._Render)

    def __del__(self):
        AnimationTool().OnUIIdle.Remove(self._Render)

    def DoRender(self):
        pass

class sceneRenderer_MixedDraw(sceneRenderer):
    def __init__(self):
        super(sceneRenderer_MixedDraw, self).__init__()
        self.scnCache = Draw.rScene()

    def __del__(self):
        self.scnCache.clear()
        super(sceneRenderer_MixedDraw, self).__del__()

    def _Render(self):
        scn = FBSystem().Scene
        rTools.BuildScene(scn, self.scnCache)

        mat = FB
