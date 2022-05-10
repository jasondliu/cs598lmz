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
    import View, Item, Group, HGroup, VGroup, ListEditor, HSplit, VSplit

from pyface.api \
    import ImageResource

from pyface.image_resource \
    import ImageResource

from pyface.ui.qt4.util.gui_test_assistant \
    import GuiTestAssistant

from pyface.ui.qt4.util.gui_test_assistant \
    import activate_window

from pyface.ui.qt4.util.gui_test_assistant \
    import get_image_pattern

from pyface.ui.qt4.util.gui_test_assistant \
    import is_qt4

from pyface.ui.qt4.util.gui_test_assistant \
    import
