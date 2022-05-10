import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Str, Property, cached_property, Instance, \
           List, Any, Int, Bool, Event, on_trait_change, Tuple, Enum

from traitsui.api \
    import View, Item, HGroup, VGroup, Tabbed, Group, HSplit, VSplit, \
           EnumEditor, TableEditor, ObjectColumn, InstanceEditor, TextEditor, \
           spring, Label, Handler, ButtonEditor, Action, Menu, MenuBar, \
           ToolBar, ToolBarButton, StatusItem, CheckListEditor, CodeEditor, \
           ListEditor, spring_width

from traitsui.table_column \
    import ObjectColumn

from traitsui.table_filter \
    import TableFilter, RuleTableFilter, RuleFilterTemplate, \
           MenuFilterTemplate, EvalFilterTemplate, EvalTableFilter

from traitsui.
