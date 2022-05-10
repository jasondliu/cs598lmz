import mmap
import os
import re
import sys
import time

from collections import defaultdict
from datetime import datetime
from itertools import chain
from subprocess import Popen, PIPE

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from pombola.core.models import Person, Position, PositionTitle, Place
from pombola.core.models import Organisation, OrganisationKind
from pombola.core.models import OrganisationRelationship
from pombola.core.models import ContactKind, Contact
from pombola.core.models import InformationSource
from pombola.core.models import PersonName
from pombola.core.models import PlaceKind
from pombola.core.models import PositionTitle
from pombola.core.models import Position
from pombola.core.models import OrganisationKind
from pombola.core.models import Organisation
from pombola.core.models import OrganisationRelationship
from pombola.core.models import ContactKind
from pombola.core.models import Contact
