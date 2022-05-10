import weakref
import itertools
import logging
import os
import re
import sys
import traceback

from twisted.internet import reactor, defer
from twisted.internet.defer import Deferred, DeferredList
from twisted.internet.task import LoopingCall
from twisted.python.failure import Failure
from twisted.python.threadable import isInIOThread

from buildbot.process.properties import Properties, Property
from buildbot.process.properties import WithProperties
from buildbot.process.results import CANCELLED, EXCEPTION, FAILURE, SKIPPED, SUCCESS
from buildbot.process.results import worst_status
from buildbot.process.step import BuildStep, _BuildStepFactory, renderer
from buildbot.schedulers import base
from buildbot.schedulers.forcesched import ForceScheduler, StringParameter
from buildbot.status.results import SUCCESS as RESUME
from buildbot.util import ascii2unicode, unicode2bytes
