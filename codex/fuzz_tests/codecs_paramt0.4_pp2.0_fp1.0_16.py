import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

from django.core.management import setup_environ
import settings
setup_environ(settings)

from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from myrobogals.rgchapter.models import Chapter, ChapterPresident, ChapterSecretary, ChapterWeb, ChapterTreasurer, ChapterPublicRelations
from myrobogals.rgmain.models import School, SchoolAdmin, UserList
from myrobogals.rgmessages.models import EmailMessage, EmailMessageRecipient
from myrobogals.rgteaching.models import SchoolVisit, SchoolVisitReport
from myrobogals.rgprofile.models import UserProfile, UserPhone, UserAddress, UserEducation, UserWork, UserInterest
from myrobogals.rgchapter.models import Chapter
from myrobogals.rgprofile.models import User
from myrobogals.rg
