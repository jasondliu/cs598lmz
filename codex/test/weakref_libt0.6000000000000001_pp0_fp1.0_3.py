import weakref
import types
import traceback

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

# The global list of all registered traits:
TraitList = []

# The global list of all trait change handlers:
TraitChangeHandlers = []

# The global list of all post-trait change handlers:
PostTraitChangeHandlers = []

# Global list of all traits that have been copied:
CopiedTraits = []

# The global list of all trait notifiers:
TraitNotifiers = []

# The global list of all trait listeners:
TraitListeners = []

# The global list of all trait listeners:
TraitPrefixListeners = []

# The global list of all traits that have been set:
SetTraits = []

# The global list of all traits that have been set:
GetTraits = []

# The global list of all trait prefixes that have been set:
SetPrefixTraits = []

# The global list of all trait prefixes that have been set:
GetPrefixTraits = []

# The global list of
