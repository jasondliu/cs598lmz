import weakref

from . import epsilon
from . import effector
from . import expression
from . import motor
from . import port
from . import script
from . import util


from . import zencad

from zencad.lazifier import lazifier

from zencad import util
from zencad.util import zencad_epsilon
from zencad.util import typechecker

from zencad.lazifier.base import *
from zencad.lazifier.contour import *
from zencad.lazifier.solid import *
from zencad.lazifier.parametrize import *
from zencad.lazifier.dynamic import *
from zencad.lazifier.bound_box import *
from zencad.lazifier.util import *


from zencad.lazifier.describe import *



try:
	return __all__, __version__
except:
	return None, None
