import gc, weakref

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, HasStrictTraits, Any, Instance, List, Str, \
           Property, cached_property, on_trait_change

from traitsui.api \
    import View, Item, Group, HGroup, VGroup, VSplit, Tabbed, \
           HSplit, TableEditor, ObjectColumn, InstanceEditor, Handler, \
           EnumEditor, spring, Label, UItem, spring_y

from traitsui.table_column \
    import ObjectColumn

from traitsui.menu \
    import Action, Menu, MenuBar

from traitsui.tabular_adapter \
    import TabularAdapter

from traitsui.extras.checkbox_column \
    import CheckboxColumn

from traitsui.table_filter \
    import TableFilter, RuleTableFilter, RuleFilterTemplate, \
           MenuFilterTemplate, EvalFilterTemplate, EvalTableFilter

from traitsui.table_filter \
    import RuleTableFilter, RuleFilterTemplate,
