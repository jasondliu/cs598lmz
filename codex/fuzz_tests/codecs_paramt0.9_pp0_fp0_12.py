import codecs
codecs.register_error("strict", codecs.ignore_errors)

import os.path
from os.path import **
from basic_hash import BasicHasher

from pprint import pprint
from twisted.internet import reactor
from twisted.web import client
from twisted.application import service, internet
from twisted.web import server
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET
import misc
from stats import Stats, Rate
from p2p_connection import p2p_bootstrap

from logging import warn, info

from twisted.web.error import Error
from zope.interface import implements
from twisted.web.iweb import ICredentialFactory
from twisted.cred.portal import IRealm
from twisted.cred.portal import Portal
from twisted.cred.checkers import InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.credentials import IUsernamePassword, IUsernameHashedPassword, UsernamePassword, UsernameHashedPassword
from twisted.cred.plugins.digest import DigestCredentialFactory
from twisted.cred.check
