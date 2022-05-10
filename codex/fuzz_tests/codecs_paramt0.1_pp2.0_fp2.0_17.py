import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, Instance, List, Property, cached_property

from traitsui.api \
    import View, Item, Group, HGroup, VGroup, VSplit, Tabbed, HSplit, \
           EnumEditor, TextEditor, CodeEditor, TreeEditor, TreeNode, \
           ObjectTreeNode, ListEditor, ListStrEditor, InstanceEditor

from traitsui.menu \
    import Menu, Action, Separator

from traitsui.tabular_adapter \
    import TabularAdapter

from traitsui.tree_node \
    import NewAction, CopyAction, CutAction, PasteAction, DeleteAction

from pyface.api \
    import ImageResource, confirm, error, warning, YES, NO, CANCEL

from pyface.image_resource \
    import ImageResource

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from py
