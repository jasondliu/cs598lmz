import types
types.ModuleType             # This is how to create a module object
 
from types import ModuleType  # Or import it from types
m = ModuleType("spam")        # Create a module object
m.x = 2                      # Set an attribute named x in m
m.x
import sys                    # Get the sys module
sys.modules["spam"] = m       # Register m in the sys.modules table
sys.modules["spam"]
import spam                   # Import m (now)
spam.x                        # Namespace dict is m.__dict__
spam                          # The actual module object
