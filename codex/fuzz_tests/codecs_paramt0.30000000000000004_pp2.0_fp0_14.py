import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import config
from . import log
from . import util
from . import version

from . import commands
from . import context
from . import error
from . import hgweb
from . import i18n
from . import mail
from . import patch
from . import phases
from . import scmutil
from . import sshserver
from . import templatekw
from . import ui as uimod
from . import url
from . import wireproto
from . import wsgicgi
from . import wsgirefserver
from . import wsgiserver

from .i18n import _
from .node import hex, nullid, nullrev, short
from .pycompat import getattr
from .utils import (
    procutil,
    stringutil,
)

# import after i18n
from . import (
    bookmarks,
    bundle2,
    changegroup,
    changelog,
    cmdutil,
    color,
    commandserver,
    copies,
    demandimport,
    discovery,

