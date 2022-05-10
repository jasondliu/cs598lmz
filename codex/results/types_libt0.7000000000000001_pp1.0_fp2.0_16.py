import types
types.ModuleType.__dict__.__setitem__('__package__', None)

# py2exe fix
import os
if os.path.exists('db.sqlite'):
    os.unlink('db.sqlite')

from bdpy_gui.app import main
main()
