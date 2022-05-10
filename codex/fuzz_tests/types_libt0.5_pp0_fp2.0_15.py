import types
types.ModuleType

# The default import hook for extension modules
import sys
sys.__import__

# The default import hook for frozen modules
import sys
sys.__import_frozen__

# The default import hook for built-in modules
import sys
sys.__import_builtin__

# The default import hook for pkgutil
import pkgutil
pkgutil.__import__

# The default import hook for importlib
import importlib
importlib.__import__

# The default import hook for importlib.abc
import importlib.abc
importlib.abc.__import__

# The default import hook for importlib.machinery
import importlib.machinery
importlib.machinery.__import__

# The default import hook for importlib.util
import importlib.util
importlib.util.__import__

# The default import hook for importlib.extension
import importlib.extension
importlib.extension.__import__

# The default import hook for importlib.abc.Finder
import importlib.abc
importlib.abc.
