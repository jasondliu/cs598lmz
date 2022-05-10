import gc, weakref

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from traits.api \
    import HasPrivateTraits, Instance, Property, List, Str, Any, Bool, \
           Event, on_trait_change, cached_property, Delegate, \
           TraitError, TraitListEvent, TraitDictEvent, TraitPrefixList

from traits.trait_base \
    import SequenceTypes

from traits.trait_errors \
    import TraitNotificationError

from traitsui.api \
    import View, Item, Group, Handler, UIInfo, UItem, VGroup, HGroup, \
           HSplit, VSplit, Tabbed, TabbedPanel, ViewSubElement, \
           ViewElement, ViewElements, ViewElementList, ViewElementTitle, \
           ViewElementHandler, ViewState, ViewStateList, ViewStateHandler, \
           ViewStateItem, ViewStateElement, ViewStateElements, \
           ViewStateElementList, ViewStateElementHandler, ViewStateElementTitle

from traitsui.editors.api \
    import
