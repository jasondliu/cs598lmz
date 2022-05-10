import weakref
import sys
import os
import os.path
import cPickle as pickle
import threading
import traceback
import logging
import util
import util.threads
import util.primitives.error_handling as error_handling
import util.callbacks as callbacks
import traceback

log = logging.getLogger('serialize')

# NOTE: Somehow we need a unique list of objects at any given time;
# we can't just serialize all of them, because they may have
# dependencies that aren't yet serialized - or they may have
# serialized themselves and we don't need to serialize them again.

# Also, we need an instance-specific list of objects, because the
# order in which they are serialized matters - if we serialize
# 'foo' before 'bar', then it better be the case that 'bar' depends
# on 'foo', or else deserialization won't work.

# this seems like a reasonable scheme:
#   - have a global dict of objects, keyed by id(obj)
#   - have a instance-specific set of objects that are currently
