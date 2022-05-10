import gc, weakref

from . import _pywrapcppyy as cppyy

#-----------------------------------------------------------------------------
# memory management

def _get_memory_policy():
    """Return the current memory policy."""
    return cppyy.gbl.gROOT.GetMemoryPolicy()

def _set_memory_policy(policy):
    """Set the memory policy.

    This function is used to set the memory policy for the current scope.
    The policy will be reset to the value it had when this function was
    called when the function exits.

    Parameters
    ----------
    policy : int
        The memory policy to set. This can be one of the following:
        - cppyy.gbl.kMemoryStrict: memory is allocated and owned by the
          python object.
        - cppyy.gbl.kMemoryHeuristics: memory is allocated by the python
          object, but ownership is transferred to the C++ object.
        - cppyy.gbl.kMemoryHeuristics2: memory is allocated by the python
          object, but ownership is transferred to the C++ object.
        - cppy
