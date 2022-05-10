import gc, weakref

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Instance, Property, List, Any, cached_property, \
           Event, Bool, Button, on_trait_change

from traitsui.api \
    import View, Item, HGroup, VGroup, VSplit, Tabbed, Group, \
           InstanceEditor, EnumEditor, spring, Label

from traitsui.menu \
    import Menu, Action

from traitsui.tabular_adapter \
    import TabularAdapter

from traitsui.extras.checkbox_column \
    import CheckboxColumn

from etsdevtools.developer.tools.profiler \
    import Profile

from etsdevtools.developer.api \
    import FilePosition

from etsdevtools.developer.helper.file_position \
    import get_file_position

from etsdevtools.developer.helper.profiler \
    import profile_stats

from etsdevtools.developer.helper
