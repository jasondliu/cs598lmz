import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, Unicode, Bool, Instance, List, Any, \
           Property, cached_property, on_trait_change

from traitsui.api \
    import View, Item, Group, ListEditor, TreeEditor, TreeNode

from traitsui.menu \
    import Action, Menu, MenuBar

from pyface.api \
    import FileDialog, OK, ImageResource

from pyface.image_resource \
    import ImageResource

from pyface.ui.qt4.util.gui_test_assistant \
    import GuiTestAssistant

from pyface.ui.qt4.util.image_cache \
    import ImageCache

from pyface.ui.qt4.tree_editor \
    import SimpleEditor as TreeEditor

from pyface.ui.qt4.tree_node \
    import SimpleNode as TreeNode

from pyface.ui.qt4.code_editor.code
