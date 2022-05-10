import weakref

import numpy as np

# Import traits and traitsui
from traits import HasTraits, Str, Int, Float, \
                    Bool, Trait, on_trait_change, \
                    Property, Instance, List, DelegatesTo, \
                    CSSList, Any, File, Tuple, cached_property
import traitsui
from traitsui.api import View, Item, Spring, Group, VGroup, \
                            CheckListEditor, EnumEditor, \
                            TextEditor, HGroup, UItem, VSplit, \
                            ListEditor, Tabbed, Label, spring, \
                            InstanceEditor, TableEditor, Tabbed
from traitsui.editors.table_editor import SetEditor

# Import Chaco
from chaco.api import ArrayPlotData, Plot, ArrayDataSource
from chaco.tools.api import PanTool, ZoomTool, LegendTool
from chaco.scales.api import LinearScale, CalendarScaleSystem
from chaco.scales_tick_generator import ScalesTickGenerator
from chaco.default_colormaps import *
#
