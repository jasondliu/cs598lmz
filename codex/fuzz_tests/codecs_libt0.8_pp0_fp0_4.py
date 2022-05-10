import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

#import pdb; pdb.set_trace()

#sys.setdefaultencoding('utf8')

import sys
import os
import random
import re
import shutil
import urllib2

from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify

APPINDICATOR_ID = "assistive-reading"

def main():
    # python3-gi-cairo should be installed
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('/home/username/Downloads/translator_indicator/assets/lips.png'), appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    Notify.init(APPIND
