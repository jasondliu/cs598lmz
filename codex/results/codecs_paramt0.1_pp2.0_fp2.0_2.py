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
           ObjectTreeNode, ListEditor, ListStrEditor, InstanceEditor

from traitsui.menu \
    import Action, Menu, MenuBar, NoButtons

from traitsui.file_dialog \
    import open_file, save_file

from traitsui.key_bindings \
    import KeyBinding, KeyBindings

from pyface.api \
    import ImageResource, confirm, error, warning, information, YES, NO, CANCEL

from pyface.image_resource \
    import ImageResource

from pyface.timer.api \
    import do_later

from pyface.ui.qt4
