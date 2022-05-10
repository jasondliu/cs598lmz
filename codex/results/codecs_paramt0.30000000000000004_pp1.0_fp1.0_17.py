import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasTraits, Str, Bool, List, Instance, Property, Any, Event, \
           on_trait_change

from traitsui.api \
    import View, Item, Group, HGroup, VGroup, VSplit, Tabbed, EnumEditor, \
           TextEditor, CodeEditor, HSplit, Handler, TreeEditor, TreeNode, \
           TreeNodeObject

from traitsui.menu \
    import Menu, Action

from traitsui.wx.tree_editor \
    import NewAction, CopyAction, CutAction, PasteAction, DeleteAction, \
           RenameAction, ExpandAction, CollapseAction

from traitsui.wx.constants \
    import OKColor, ErrorColor

from traitsui.wx.editor \
    import Editor

from traitsui.wx.basic_editor_factory \
    import BasicEditorFactory

from traitsui.wx.helper \
    import TraitsUIPan
