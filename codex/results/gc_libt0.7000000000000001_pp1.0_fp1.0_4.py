import gc, weakref
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.widgets import Slider, Button

%matplotlib notebook

from . import SpaceTimeMesh, SpaceTimeMesh2D
from . import _pyflib
from .utils import _display, _animate
from .utils import _sep, _present, _create_folder, _create_file, _get_filename
from .utils import _get_from_string_or_list, _is_string_or_list, _is_string
from .utils import _is_number, _is_list, _is_callable
from .utils import _convert_to_list
from .utils import _is_2d, _is_vector, _is_scalar, _is_plot_type
from .utils import _is_2d_list, _is_2d_array
from .utils import _is_
