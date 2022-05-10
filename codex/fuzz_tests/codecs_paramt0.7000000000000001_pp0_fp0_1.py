import codecs
codecs.register_error('suppl', codecs.replace_errors)

import csv
from csv import DictReader
import cStringIO
from collections import defaultdict

import sys
import os
from datetime import datetime
import re

import itertools
import requests
from lxml import etree

from opencontext_py.libs.rootpath import RootPath
from opencontext_py.libs.general import LastUpdatedOrderedDict
from opencontext_py.libs.filecache import FileCache
from opencontext_py.libs.globalmaptiles import GlobalMercator
from opencontext_py.libs.isoyears import ISOyears
from opencontext_py.libs.chronotiles import ChronoTile
from opencontext_py.apps.ocitems.manifest.models import Manifest
from opencontext_py.apps.ocitems.strings.models import OCstring
from opencontext_py.apps.ocitems.persons.models import Person
from opencontext_py.apps.ocitems.projects.models import Project
from opencontext_py.apps.ocitems.predicates.models import
