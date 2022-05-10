import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import re
from datetime import datetime
from bs4 import BeautifulSoup

from django.db import connection, transaction
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import six


from ls.joyous.models import RecurringEvent, MultidayEvent, Calendar
from ls.joyous.utils import getSite, getHolidaysCalendar
from ls.joyous.utils.recurrence import Recurrence
import telegram
import time
from telegram_bot.models import TelegramSubscriptions
from telegram_bot.utils import send_message_to_subscribers, send_message_to_subscriber
from telegram_bot.settings import bot
from ls.joyous.models import RecurringEvent, MultidayEvent, Calendar
from ls.joyous.utils import getSite, getHolidaysCalendar
from ls.joyous.utils.recurrence
