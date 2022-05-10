import gc, weakref
import pygame
from pygame.locals import *

from pygame.sprite import Sprite
from pygame.sprite import DirtySprite
from pygame.sprite import Group
from pygame.sprite import LayeredUpdates
from pygame.sprite import LayeredDirty
from pygame.sprite import OrderedUpdates
from pygame.sprite import OrderedDirty
from pygame.sprite import RenderUpdates
from pygame.sprite import RenderPlain
from pygame.sprite import GroupSingle
from pygame.sprite import GroupSingleDirty
from pygame.sprite import GroupSingleLayered
from pygame.sprite import GroupSingleLayeredDirty
from pygame.sprite import GroupSingleOrdered
from pygame.sprite import GroupSingleOrderedDirty
from pygame.sprite import GroupSingleRender
from pygame.sprite import GroupSingleRenderPlain

from pygame.sprite import spritecollide
from pygame.sprite import spritecollideany
from pygame.sprite import spritecollideany_ordered
from pygame.spr
