import mmap
import os
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from optparse import OptionParser
from subprocess import Popen, PIPE

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.db.models import Q
from django.utils.translation import ugettext as _

from celery.task.control import inspect

from PIL import Image

from mygpo.core.models import Podcast, Episode, EpisodeState, EpisodeAction, \
    MimeType, Device, Client, Subscription, PodcastGroup, PodcastGroupItem, \
    EpisodeDownload, EpisodeFile, EpisodeFileAction, EpisodeFileState, \
    EpisodeFileDownload, DeviceSettings, EpisodeFilePlaylist, \
    EpisodeFilePlaylistItem, EpisodeFilePlaylistAction, \
    EpisodeFilePlaylistState, EpisodeFilePlaylistDownload, \
    EpisodeFilePlaylistItemAction, EpisodeFilePlaylistItem
