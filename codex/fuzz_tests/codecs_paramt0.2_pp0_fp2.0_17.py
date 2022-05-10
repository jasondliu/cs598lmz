import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join

from traits.api \
    import HasPrivateTraits, Str, List, Instance, Property, cached_property, \
           on_trait_change, Any, Bool, Event, Int, Tuple, Undefined, \
           Trait, TraitError, TraitListEvent, TraitPrefixList, TraitPrefixMap

from traits.trait_base \
    import SequenceTypes

from traits.trait_errors \
    import TraitNotificationError

from traits.trait_numeric \
    import Array

from traits.trait_types \
    import Delegate, DelegatesTo, Event, File, This, Type, Undefined

from traitsui.api \
    import View, Item, VGroup, HGroup, Tabbed, HSplit, VSplit, Group, \
           ListEditor, TableEditor, InstanceEditor, TreeEditor, TreeNode, \
           TreeNodeObject, TreeNode
