import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, Instance, List, Any, Property, Bool, \
           cached_property, on_trait_change, Event, DelegatesTo

from traitsui.api \
    import View, Item, Group, HGroup, VGroup, Tabbed, spring, Label, \
           Handler, Action, Menu, MenuBar, ToolBar, StatusItem, \
           ListEditor, TreeEditor, TreeNode, ObjectTreeNode, \
           ListStrEditor, EnumEditor, InstanceEditor, TextEditor, \
           CodeEditor, HTMLEditor, ImageEditor, HistoryEditor, \
           TitleEditor, RangeEditor, TableEditor, ValueEditor, \
           FileEditor, DirectoryEditor, ColorEditor, FontEditor, \
           KeyBindingEditor, HandlerEditor, ShellEditor, \
           ShellEditorItem, ShellEditorGroup, ShellEditorNotebook, \
           ShellEditorWindow, ShellEditorPage, ShellEditorNotebookEditor, \
           ShellEditor
