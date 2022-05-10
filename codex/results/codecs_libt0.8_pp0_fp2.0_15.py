import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import os.path
import getopt
import sys
import re
import csv
import cgi
import cgitb
import json
from pmr2.runtime import app
from zope.component import getUtility, getMultiAdapter
from zope.interface import Interface, implements
from zope.component import queryUtility, queryAdapter
from zope.interface import Interface, Attribute, implements
import zope.publisher.browser
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.viewlet.interfaces import IViewletManager
from zope.viewlet.viewlet import ViewletBase
from zope.app.pagetemplate import ViewPageTemplateFile
from pyramid.path import DottedNameResolver
from cornice.resource import resource, view
from repoze.catalog.query import Eq, Contains, And
from pyramid.httpexceptions import HTTPBadRequest
from urllib import urlencode
import xlrd
from datetime import
