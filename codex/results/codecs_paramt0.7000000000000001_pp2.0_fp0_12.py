import codecs
codecs.register_error("strict", codecs.ignore_errors)

# Jython bug workaround. See #17134.
from org.python.core import PySystemState
PySystemState.registry.put("python.console.encoding", "UTF-8")

def add_path(p):
    if not p in sys.path:
        sys.path.insert(0, p)

# .jar files
add_path(os.path.join(os.path.dirname(__file__), "jython-standalone-2.7.0.jar"))

# .py files
add_path(os.path.join(os.path.dirname(__file__), "Lib"))
add_path(os.path.join(os.path.dirname(__file__), "Lib", "site-packages"))

import org.python.util.jython as jython
import org.python.core.PySystemState as PySystemState

# Set classpath
jython.JythonClassLoader.addClassPath(os.path.join(os.path.dirname(__file__
