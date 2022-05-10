import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)
import platform
from pathlib import Path
from os import system, chdir, path

from pygame._sdl2.key import KeyConstants as sdlk

from panda3d.core import TextNode
from direct.gui.OnscreenImage import OnscreenImage
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import Sequence
from direct.interval.LerpInterval import LerpFunc
from direct.interval.IntervalGlobal import Parallel, Sequence
from direct.interval.FunctionInterval import Func, Wait
from direct.interval.IntervalGlobal import LerpScaleInterval
from direct.interval.IntervalGlobal import LerpPosInterval
from panda3d.core import Vec3,Vec4
from panda3d.core import Texture,TextureStage,Filename
from panda3d.core import CardMaker
from panda3d.core import NodePath,PandaNode
from panda3d.core import Point3, Mat4, Quat
from direct.gui.Direct
