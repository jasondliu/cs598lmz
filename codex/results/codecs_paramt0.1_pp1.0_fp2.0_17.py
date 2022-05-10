import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, List, Instance, Property, cached_property

from traitsui.api \
    import View, Item, Group, HGroup, VGroup, VSplit, Tabbed, HSplit, \
           EnumEditor, TextEditor, CodeEditor, TreeEditor, TreeNode, \
           TreeNodeObject, ObjectTreeNode, ListEditor, InstanceEditor

from traitsui.menu \
    import Menu, Action, Separator

from pyface.api \
    import ImageResource, confirm, error, warning, YES, NO, CANCEL

from pyface.image_resource \
    import ImageResource

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.ui.qt4.code_editor.code_widget import PygmentsHighlighter

from pyface.ui.qt4.code_editor.code_widget import PygmentsLexer


