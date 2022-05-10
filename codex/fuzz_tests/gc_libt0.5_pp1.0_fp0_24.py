import gc, weakref
import pymel.core as pm
import maya.cmds as cmds
import maya.OpenMaya as om
import maya.OpenMayaUI as mui
import maya.OpenMayaMPx as mpx
import maya.OpenMayaRender as mr
import maya.OpenMayaAnim as manim
import maya.OpenMayaFX as mfx
import maya.mel as mel

#===============================================================================
#
#===============================================================================
class MayaComponent():
    """
    Component wrapper class
    """
    def __init__(self, component, dagPath, dagPathComponent, dagPathComponentIndex):
        self.component = component
        self.dagPath = dagPath
        self.dagPathComponent = dagPathComponent
        self.dagPathComponentIndex = dagPathComponentIndex
        self.mobject = dagPath.node()
        self.mobjectIndex = dagPath.instanceNumber()
        self.mfnDagNode = om.MFnDagNode(self.mobject)
        self.mfnMesh = om.MFnMesh
