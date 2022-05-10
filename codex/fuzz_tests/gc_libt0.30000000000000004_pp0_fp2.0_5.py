import gc, weakref

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Any, Instance, Property, List, Bool, Event, \
           on_trait_change, cached_property, DelegatesTo, Str, Int

from traitsui.api \
    import View, VGroup, HGroup, Item, Label, Handler, UIInfo, \
           spring, TreeEditor, TreeNode, ObjectTreeNode

from traitsui.menu \
    import Menu, Action, Separator

from traitsui.tree_node \
    import NewAction, CopyAction, CutAction, PasteAction, DeleteAction, \
           RenameAction, DragAndDrop

from traitsui.editors.tree_editor \
    import TreeEditor as BaseTreeEditor

from traitsui.editors.tree_editor \
    import TreeNodeObject, TreeNodeList, TreeNodeDict, TreeNodeListObject, \
           TreeNodeSetObject, TreeNodeTupleObject, TreeNodeAny, \
           TreeNodeListAny, TreeNodeDictAny, TreeNodeListObject
