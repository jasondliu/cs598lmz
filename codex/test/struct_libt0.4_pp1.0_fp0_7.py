import _struct
import _sys
import _thread
import _time
import _types
import _weakref


# -- stdlib --
# -- third party --
# -- own --
from gamepack import getresource as _grs
from gamepack.thb import characters
from gamepack.thb.ui.ui_meta.common import gen_metafunc, my_turn
from gamepack.thb.ui.ui_meta.common import passive_clickable, passive_is_action_valid
from gamepack.thb.ui.ui_meta.common import limit1_skill_used
from gamepack.thb.ui.resource import resource as gres

# -- code --
__metaclass__ = gen_metafunc(characters.ran)


class Ran:
    # Character
    char_name = u'伊吹萃香'
    port_image = gres.ran_port
