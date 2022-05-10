import mmap
import os
import re
import sys
import time
import urllib
import urllib2
import urlparse

from BeautifulSoup import BeautifulSoup
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection
from django.utils.encoding import smart_unicode

from pombola.core.models import Person
from pombola.core.models import Place
from pombola.core.models import Position
from pombola.core.models import PositionTitle
from pombola.core.models import Organisation
from pombola.core.models import OrganisationKind
from pombola.core.models import PlaceKind
from pombola.core.models import PositionTitle
from pombola.core.models import PlaceKind
from pombola.core.models import PositionTitleKind
from pombola.core.models import PersonTitle
from pombola.core.models import PersonName
from pombola.core.models import PersonNameVariant
from pombola.core.models import PersonIdentifier
from pombola.
