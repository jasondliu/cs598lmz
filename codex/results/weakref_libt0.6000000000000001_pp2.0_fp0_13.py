import weakref

import numpy as np
import matplotlib.pyplot as plt

from . import _marker_c
from . import _line_c
from . import _text_c
from . import _image_c
from . import _path_c
from . import _patch_c
from . import _collection_c
from . import _contour_c
from . import _quiver_c
from . import _stix_c
from . import _mathtext_c
from . import _path_effects
from . import _tri_c
from . import _axes_c
from . import _axis_c
from . import _cbook
from . import _transforms
from . import _matplotlib_axes
from . import cbook
from . import docstring
from . import rcParams
from . import tight_layout
from . import rcParamsDefault
from .backend_bases import (_Backend, FigureCanvasBase,
                            FigureManagerBase, GraphicsContextBase,
                            RendererBase)
from .backend_bases import NavigationToolbar2
from
