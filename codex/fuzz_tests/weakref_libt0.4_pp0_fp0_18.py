import weakref

from . import _imaging as core
from . import _imagingmath
from . import _imagingcms
from . import _imagingdraw
from . import _imagingft
from . import _imagingtk
from . import _imagingmath
from . import _imagingmorph
from . import _imagingps
from . import _imagingtk
from . import _webp

from ._util import isPath
from ._util import isStringType

if sys.platform == "darwin":
    from ._imagingmac import (
        tk_chooseColor, tk_chooseDirectory, tk_dialog, tk_focusFollowsMouse,
        tk_getOpenFile, tk_getSaveFile, tk_messageBox, tk_root, tk_setPalette,
        tk_splitpath, tk_tksupport
    )

from . import _imagingft

##
# A simple 2-dimensional vector class.

class Vector2(object):

    def __init__(self, xy):
        self.xy =
