import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from enthought.traits.api \
    import HasPrivateTraits, Any, Str, Int, List, Instance, Property

from enthought.traits.ui.api \
    import View, Item

from enthought.traits.ui.menu \
    import NoButtons

from enthought.traits.ui.wx.editor \
    import Editor

from enthought.traits.ui.wx.basic_editor_factory \
    import BasicEditorFactory

from enthought.traits.ui.wx.editor_factory \
    import EditorFactory

from enthought.traits.ui.wx.helper \
    import TraitsUIPanel

from enthought.traits.ui.wx.key_bindings \
    import KeyBindings

from enthought.traits.ui.wx.menu \
    import Menu

from enthought.traits.ui.wx.text_
