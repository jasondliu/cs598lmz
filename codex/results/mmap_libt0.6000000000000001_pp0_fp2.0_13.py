import mmap
import os
import sys
import time
import traceback
import types

# Local imports
from . import ast
from . import common
from . import core
from . import error
from . import ext
from . import frame
from . import internal
from . import parser
from . import pydoc
from . import pyframe
from . import pygram
from . import pytoken
from . import token
from . import util
from . import version

#------------------------------------------------------------------------
#
# Global variables
#
#------------------------------------------------------------------------

# NOTE: This is not a constant because of circular dependencies
_ast_parse = ast.parse
_ast_dump = ast.dump
_ast_NodeTransformer = ast.NodeTransformer
_ast_NodeVisitor = ast.NodeVisitor
_ast_fix_missing_locations = ast.fix_missing_locations
_ast_increment_lineno = ast.increment_lineno
_ast_PyCF_ONLY_AST = ast.PyCF_ONLY_AST

_builtin_compile = compile
_builtin_exec = exec
_builtin
