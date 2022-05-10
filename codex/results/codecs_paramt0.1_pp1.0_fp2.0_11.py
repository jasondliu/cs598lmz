import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, Int, Bool, List, Instance, Any, Property

from traitsui.api \
    import View, Item, Group, HGroup, VGroup, Tabbed, HSplit, VSplit, \
           TabularEditor, ObjectColumn, on_facet_set

from traitsui.tabular_adapter \
    import TabularAdapter

from traitsui.menu \
    import Action, Menu, MenuBar

from pyface.api \
    import FileDialog, OK, ImageResource, confirm, error, YES, NO

from pyface.image_resource \
    import ImageResource

from pyface.timer.api \
    import do_later

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.ui.qt4.code_editor.code_widget import PygmentsHighlighter

from pyface.ui.qt4
