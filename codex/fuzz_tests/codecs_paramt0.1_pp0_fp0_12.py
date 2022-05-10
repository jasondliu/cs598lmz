import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, Property, cached_property, Instance, \
           List, Any, Bool, Event, on_trait_change

from traitsui.api \
    import View, Item, Group, HGroup, VGroup, VSplit, Tabbed, \
           TreeEditor, TreeNode, Handler, EnumEditor, spring, Label, \
           TextEditor, CodeEditor, InstanceEditor

from traitsui.menu \
    import Action, Menu, MenuBar

from pyface.api \
    import ImageResource, FileDialog, OK, CANCEL, YES, NO, ConfirmationDialog

from pyface.image_resource \
    import ImageResource

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.ui.qt4.code_editor.code_widget import PygmentsHighlighter

from pyface.ui.qt4.code_editor.
