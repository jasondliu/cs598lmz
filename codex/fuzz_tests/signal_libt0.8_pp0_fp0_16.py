import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from forms.ui_bibtex_import import Ui_BibTexDialog
from forms.ui_author_item import Ui_AuthorItem
from forms.ui_book_item import Ui_BookItem
from forms.ui_wizard_import import Ui_WizardImport

from widgets.book import Book
import appuifw
import sysinfo
import os
import e32
import urllib2
import bibtex
import time
from emusicdownloader.common.utils import *
from emusicdownloader.common.objects import *
from emusicdownloader.common.controllers import *
from emusicdownloader.gui.controllers import *

#defaults
DEFAULT_LOCALE_LANGUAGE = u"en"
DEFAULT_LOCALE_COUNTRY = u"US"

DEFAULT_CONFIG_FILENAME = u"
