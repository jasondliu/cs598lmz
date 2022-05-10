import gc, weakref

from pymol import cmd

from . import pymol2
from . import pymol2_cmd
from . import pymol2_gui
from . import pymol2_key
from . import pymol2_menu
from . import pymol2_session
from . import pymol2_setting
from . import pymol2_stereo
from . import pymol2_viewing
from . import pymol2_cmd_list

from .pymol2 import *
from .pymol2_cmd import *
from .pymol2_gui import *
from .pymol2_key import *
from .pymol2_menu import *
from .pymol2_session import *
from .pymol2_setting import *
from .pymol2_stereo import *
from .pymol2_viewing import *

from .pymol2_cmd_list import *

#==============================================================================

def __init_plugin__(self=None):
    '''
    '''

    #
