import gc, weakref

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Instance, Any, Property, Event, List, \
           Str, Delegate, on_trait_change, Bool

from traitsui.api \
    import View, Group, Item, HGroup, VGroup, VSplit, HSplit, Tabbed, \
           Popup, EnumEditor, TextEditor

from traitsui.menu \
    import Action, Menu, MenuBar, NoButtons

from traitsui.tabular_adapter \
    import TabularAdapter

from traitsui.toolkit \
    import toolkit

# FIXME: ToolkitEditorFactory is a proxy class defined here just for backward
# compatibility. The class has been moved to the
# traitsui.editors.custom_editor file.
from traitsui.editors.custom_editor \
    import ToolkitEditorFactory

from traitsui.undo \
    import UndoHistory

from etsdevtools.developer.api \
    import FilePosition

#----------------------------------------------------------------
