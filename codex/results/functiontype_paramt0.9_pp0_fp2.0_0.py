from types import FunctionType
list(FunctionType(lambda x: x + 5).parameters)[0].kind

# in operator can be used to check if a name is defined in a local scope.
x = 5
y = 10
'x' in vars()

# This is the end of chapter 3
###############################
#
# The code below is for chapter 4 about Modules and Mix-Ins

import sys
sys.argv[0]

# The following is a test for import statements and showing their syntax
from sys import argv
from sys import (
    argv,
    exc_info,
    exit,
    path,
    version_info,
    )
import os.path
import os.path as op
from sys import path, argv
from sys import (
    path,
    argv,
    )
# If an import statement is to the right of another in the same line, it
# causes a syntax error.
import sys, os
from math import (
    pi as Pi,
    e as Exponent)
from math import pi as Pi, log as Log10
from math import pi as Pi, log as
