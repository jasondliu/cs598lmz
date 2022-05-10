import _struct
import ctypes
import ctypes.wintypes
import msvcrt

from lib2to3 import pytree
from lib2to3.pgen2 import token
from lib2to3.pygram import python_symbols as syms
from lib2to3.refactor import RefactoringTool, get_fixers_from_package

from . import fixers
from . import pytree_utils as pt


class InMemoryRefactoringTool(RefactoringTool):
  """A RefactoringTool that operates in memory.

  Allows the caller to specify the Python source file as a string rather than
  requiring a disk file.
  """

  def __init__(self, fixer_names=None, options=None):
    if fixer_names is None:
      fixer_names = fixers.get_all_fix_names('lib')
    fixer_names = fixers.fixers_validate(fixer_names)
    fixers = get_fixers_from_package('lib2to3.fixes')
    fixers.extend(get_fix
