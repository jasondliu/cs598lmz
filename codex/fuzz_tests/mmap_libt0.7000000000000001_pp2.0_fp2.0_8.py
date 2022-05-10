import mmap
import re
import os.path
import optparse
import pygraphviz as gv

# This script is intended to be used to find out what is the minimum required
# set of modules to perform a specific function.

# It performs a BFS traversal of the dependency tree, starting at the module
# specified on the commandline.

# It will generate a PNG image of the dependency tree, with nodes colored based
# on whether they are required to perform the function or not.

# Nodes marked green are required, nodes marked red are not required to perform
# the specified function.

# Nodes marked yellow are required to perform the function but are not required
# for any other function.

# The --force-module option can be used to include any module in the final
# dependencies.

# The --remove-module option can be used to remove a dependency from the final
# dependencies.

# The --remove-function option can be used to remove all dependencies of the
# specified function from the final dependencies.

# A white node is not required to perform the function, but is required by a
# module that is required
