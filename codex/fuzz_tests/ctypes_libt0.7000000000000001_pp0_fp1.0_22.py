import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import numpy as np

from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backend_bases import NavigationToolbar2
from matplotlib.backend_bases import Event
from matplotlib.backend_bases import MouseEvent
from matplotlib.backend_bases import KeyEvent
from matplotlib.backend_bases import PickEvent
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from .widgets import Window
from .widgets import Frame
from .widgets import Button
from .widgets import Label
from .widgets import Text
from .widgets import ScrollBar
from .widgets import Scale
from .widgets import CheckButton
from .widgets import RadioButton
from .widgets import Entry
from .widgets import List
from .widgets import ProgressBar
from .widgets import Menu
from .widgets import ImageLabel
from
