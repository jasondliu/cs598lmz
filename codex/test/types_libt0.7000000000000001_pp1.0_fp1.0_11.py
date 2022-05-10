import types
types.ModuleType('test')

# Changing a module name
import sys
sys.modules['test'] = sys.modules['types']
