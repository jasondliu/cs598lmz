import select
# Test select.select()
#
# RETURN VALUES:
#
# Returns: three lists of objects that are ready:
# objects that are ready for reading
# objects that are ready for writing
# objects that have an exceptional condition
#
# If the time limit is reached with no activity, three empty lists
# are returned.
#
# The objects are always returned in the same order in which they were given.

# select.select(rlist, wlist, xlist[, timeout])

#!/usr/bin/python2
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

# Initialization

import sys
import os
import fcntl
import socket
import logging

# config
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
