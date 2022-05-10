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
    import View, Item, Group, HGroup, VGroup, VSplit, Tabbed, \
           HSplit, TableEditor, ObjectColumn, on_facet_set

from traitsui.table_column \
    import ObjectColumn

from traitsui.table_filter \
    import TableFilter, RuleTableFilter, RuleFilterTemplate, \
           MenuFilterTemplate, EvalFilterTemplate, EvalTableFilter

from traitsui.menu \
    import Menu, Action

from traitsui.extras.checkbox_column \
    import CheckboxColumn

from pyface.api \
    import FileDialog, OK, ImageResource

from pyface.image_resource \
    import ImageResource

from pyface.ui.qt4.image_resource \
    import ImageResource as QImage
