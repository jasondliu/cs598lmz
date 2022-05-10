import weakref

from pyglet import gl
from pyglet.graphics import draw
from pyglet.graphics import Batch
from pyglet.graphics import Group
from pyglet.graphics import OrderedGroup
from pyglet.graphics import TextureGroup
from pyglet.graphics import VertexList

from cocos.director import director
from cocos.layer import Layer
from cocos.rect import Rect
from cocos.euclid import Point2
from cocos.euclid import Vector2
from cocos.euclid import Matrix3
from cocos.euclid import Point3
from cocos.euclid import Vector3
from cocos.euclid import Matrix4

from cocos.sprite import Sprite
from cocos.sprite import Sprite3D

from cocos.cocosnode import CocosNode

from cocos.collision_model import AARectShape
from cocos.collision_model import CircleShape
from cocos.collision_model import CollisionManager

from cocos.actions import *
