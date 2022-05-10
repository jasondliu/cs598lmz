import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, List, Instance, Property, cached_property

from traitsui.api \
    import View, Item, HGroup, VGroup, Group, Label, spring, \
           HSplit, VSplit, Tabbed, EnumEditor

from traitsui.menu \
    import Action, Menu, MenuBar

from pyface.api \
    import ImageResource, FileDialog, OK, CANCEL, YES, NO

from pyface.image_resource \
    import ImageResource

from pyface.ui.wx.grid.api \
    import GridModel

from pyface.ui.wx.grid.grid \
    import Grid

from pyface.ui.wx.grid.bool_grid_renderer \
    import BoolGridRenderer

from pyface.ui.wx.grid.text_grid_renderer \
    import TextGridRenderer

from pyface.ui.wx
