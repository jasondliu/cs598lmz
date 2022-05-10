import gc, weakref

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api \
    import HasPrivateTraits, Any, Instance, List, Property, Str, cached_property

from enthought.traits.ui.api \
    import View, Item, Group, VGroup, HGroup, VSplit, Tabbed, Handler, \
           spring, Label, HSplit, TableEditor, ObjectColumn, on_trait_change

from enthought.traits.ui.table_column \
    import ObjectColumn

from enthought.traits.ui.menu \
    import Menu, Action, Separator

from enthought.traits.ui.tabular_adapter \
    import TabularAdapter

from enthought.traits.ui.ui_editors.array_view_editor \
    import ArrayViewEditor

from enthought.traits.ui.ui_editors.tree_editor \
    import TreeEditor

from enthought.traits.ui.ui_editors.table_editor \
