import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is intended to test the gc module's ability to collect
# various types of objects.  It is not intended to test the ability
# of the garbage collector to collect a large number of objects in
# general.  See test_gc.py for that.

import unittest
import sys
import gc
import weakref
import operator
import copy
import os
import subprocess
import time
import warnings
import types
import struct
import pickle
import io
import contextlib
import functools
import test.support
import test.support.script_helper
import test.support.gc_list
import test.support.check_warnings
import test.support.gc_collect
import test.support.gc_min_heap_size
import test.support.gc_min_objects
import test.support.gc_can_move
import test.support.gc_disable
import test.support.gc_state
import test.support.gc_object_stats
import test.support.gc_object_leak
import test.support.gc_object_tracker
import
