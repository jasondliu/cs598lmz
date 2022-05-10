import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join

from traits.api \
    import HasPrivateTraits, Str, List, Instance, Property, cached_property

from traitsui.api \
    import View, Item, Group, HGroup, VGroup, VSplit, Tabbed, HSplit, \
           EnumEditor, spring, Label

from traitsui.menu \
    import Action

from pyface.api \
    import ImageResource, FileDialog, OK, DirectoryDialog, confirm, error, \
           YES, CANCEL

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.
