import gc, weakref
from omega import getEventDispatcher, getNodeUtil, getSceneManager, \
    getSceneEventDispatcher, getUiEventDispatcher
from omegaToolkit import ui
from cyclops import SceneManager, EventDispatcher, Light, LightType,\
    RayPickVisitor, MaterialManager, Material
from euclid import Vector3, Matrix4, Point2, Point3, Ray3, Quaternion
import block, util, blocks
from util import *
from transBlock import transBlock
     
# main scene manager
scnMgr = getSceneManager()
# blocks map
blockMap = {}
# selected block
selBlock = None
# lightweight map for blocks that are being held
hlBlockList = []
init() 

setEventFunction(onEvent)
