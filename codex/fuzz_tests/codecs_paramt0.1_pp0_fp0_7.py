import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, List, Instance, Property, cached_property

from traitsui.api \
    import View, Item, Group, HGroup, VGroup, Tabbed, HSplit, VSplit, \
           EnumEditor, TextEditor, CodeEditor, TreeEditor, TreeNode, \
           ObjectTreeNode, ListEditor, ListStrEditor, Handler, Action, \
           Menu, MenuBar, ToolBar, StatusItem

from traitsui.menu \
    import OKButton, CancelButton, UndoButton, RevertButton, HelpButton

from traitsui.tabular_adapter \
    import TabularAdapter

from traitsui.tree_node \
    import NewAction, CopyAction, CutAction, PasteAction, DeleteAction

from traitsui.editors.tree_editor \
    import NewObject

from traitsui.key_bindings \
    import KeyBinding, KeyBindings

from pyface.api \
