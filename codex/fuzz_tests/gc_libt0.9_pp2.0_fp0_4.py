import gc, weakref

from panda3d.core import *

from toontown.toonbase import ToontownGlobals


class BillboardEffect:

    def __init__(self, billboardAxis=2, sortOrder=0, textureStage=0,
                 billboardNode=None, decalEffect=0):
        self.billboardAxis = billboardAxis
        if decalEffect:
            # decalEffects need to be in their own scene graph node, else they
            # will get sorted above non-decalEffects
            billboardNode = render.attachNewNode(
                "decalBillboardNode" + str(id(self)))
        self.sortOrder = sortOrder
        self.textureStage = textureStage
        self.decalEffect = decalEffect
        if not billboardNode:
            billboardNode = render.attachNewNode(
            "billboardNode" + str(id(self)))
            billboardNode.setBin('fixed', sortOrder)
            billboardNode.setDepthWrite(0)
            billboardNode.setTwoSided(0)
        self.billboardNodePath =
