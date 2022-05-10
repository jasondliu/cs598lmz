import codecs
codecs.register_error("strict", codecs.ignore_errors)
import functools
from collections import deque
import sys
from select import select

from OpenSSL import SSL, crypto

from zope.interface import (
    Attribute,
    Interface,
    )

from pyparsing import ParseException

from twisted.trial.util import SpinMixin
from twisted.trial import unittest
from twisted.internet.error import ConnectionDone
from twisted.internet.task import Clock
from twisted.internet.interfaces import (
    IAddress,
    IReactorTime,
)
from twisted.internet.defer import (
    inlineCallbacks,
    returnValue,
    succeed,
    Deferred,
    )
from twisted.internet.ssl import CertificateOptions, Certificate
from twisted.internet.tcp import Client, _AbortingMixin
from twisted.internet.selectreactor import SelectReactor
from twisted.test.iosim import connectedServerAndClient
from twisted.internet.address import IPv4Address
from twisted.python.filepath import FilePath

from foolscap.furl import decode
