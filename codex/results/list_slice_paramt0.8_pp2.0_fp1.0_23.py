import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
a=[1,2,3]
del a[:-1]
from sprocket.controlling import mod_intercept
from sprocket.controlling.tracker import Tracker
from sprocket.stages import Init
from sprocket.controlling import (Trace, Tron, TronConfig, add_tron,
        add_trace, config_trace, config_tron, run_tron, run_trace,
        configure_tracker)
from sprocket.config import settings, Configurable
from sprocket.config.option import Bool, Int, Str, List, Dict, OptionError
from twisted.trial import unittest
from twisted.internet import defer
from twisted.python import failure
from twisted.application import service
from sprocket.stages import Init, Final
from sprocket.config import settings, Configurable
from sprocket.controlling.tracker import Tracker
from sprocket.controlling import config_trace, run_trace
from sprocket.util import constants as const
from sprocket.util.misc import suppress_stdout
from sp
