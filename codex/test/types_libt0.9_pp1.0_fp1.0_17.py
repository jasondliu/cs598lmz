import types
types.StringTypes += (type(u''), )

from urllib import quote_plus
from datetime import datetime
import logging
import time

from django.conf import settings
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

import askbot
from askbot.conf import settings as askbot_settings
from askbot.utils import url_utils
from askbot.models.user import Activity
from askbot.models.post import PostRevision
from askbot.models.reply_by_email import create_reply_by_email_address
from askbot import const
from savoy.utils.strings import increment_str
from savoy.core.mail import send_email_with_template
from savoy.contrib.mailinglists.models import MailingList
from savoy.utils.mail import get_reply_address
