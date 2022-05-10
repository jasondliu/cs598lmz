import weakref
import urllib
from urllib import parse
import re
import sqlite3
import sys
import os
import shutil

from medusa import logger
from medusa import db
from medusa.common import USER_AGENT
from medusa.exceptions import ex
from medusa.network_timezones import update_network_dict
from medusa.providers.generic_provider import GenericProvider
from medusa.helper.exceptions import AuthException

# FIXME
anidb_exceptions = (
    'Banned',
    'Banned until',
    'Bad login',
    'Account disabled',
    'Account suspended',
    'No access to list',
    'Invalid credentials',
)

# FIXME
anidb_timezones = {
    'Central European Time': 'CET',
    'Eastern European Time': 'EET',
    'Eastern Standard Time': 'EST',
    'Japan Standard Time': 'JST',
    'British Summer Time': 'BST',
    'Pacific Standard Time': 'PST',
    'Australian Eastern Standard
