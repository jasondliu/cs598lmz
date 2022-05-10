import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, List, Instance, Property, Any, \
           cached_property, on_trait_change, Bool, Enum, Int, Tuple, \
           Event, DelegatesTo, Undefined

from traitsui.api \
    import View, Item, Group, VGroup, HGroup, Tabbed, HSplit, VSplit, \
           TableEditor, ObjectColumn, Handler, Action, Menu, ToolBar, \
           on_trait_change, spring, Label, ListEditor

from traitsui.table_column \
    import ObjectColumn

from traitsui.menu \
    import Menu, Action

from pyface.api \
    import ImageResource, confirm, error, warning, YES, NO, CANCEL

from pyface.image_resource \
    import ImageResource

from pyface.ui.qt4.action.api \
    import Action as QAction

from pyface.ui
