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
    import View, Item, Group, HGroup, VGroup, VSplit, Tabbed, EnumEditor

from traitsui.menu \
    import OKButton, CancelButton

from pyface.api \
    import FileDialog, OK

from pyface.image_resource \
    import ImageResource

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.ui.qt4.code_editor.code_
