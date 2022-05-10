import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, List, Instance, Property, Any, \
           cached_property, on_trait_change

from traitsui.api \
    import View, Item, Group, HGroup, VGroup, VSplit, Tabbed, \
           TreeEditor, TreeNode, ObjectTreeNode, \
           EnumEditor, TextEditor, CodeEditor, \
           Handler, Action, Menu, MenuBar, ToolBar

from traitsui.menu \
    import NoButtons

from traitsui.key_bindings \
    import KeyBinding, KeyBindings

from pyface.api \
    import FileDialog, OK, ImageResource, confirm, error, warning, YES, NO

from pyface.image_resource \
    import ImageResource

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.ui.qt4.code_editor.code_widget \
