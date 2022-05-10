import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, List, Instance, Any, Property, Bool, \
           on_trait_change, cached_property

from traitsui.api \
    import View, Item, Group, HGroup, VGroup, VSplit, Tabbed, \
           HSplit, EnumEditor, InstanceEditor, TextEditor, spring

from traitsui.menu \
    import Action, Menu, MenuBar

from pyface.api \
    import ImageResource, confirm, error, information, warning, YES, NO, CANCEL

from pyface.ui.qt4.code_editor.code_widget \
    import CodeWidget

from pyface.ui.qt4.code_editor.code_widget import CodeWidget

from pyface.ui.qt4.code_editor.code_widget import CodeWidget

from pyface.ui.qt4.code_editor.code_widget import CodeWidget

from pyface.
