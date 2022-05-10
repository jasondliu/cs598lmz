import types
types.MethodType(__builtin__.__import__, None)

# This is the code I want to run
import sys
sys.modules['__builtin__'].__dict__['__import__'] = None

# After this, I can't import anything
import types
types.MethodType(__builtin__.__import__, None)
