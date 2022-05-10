import weakref

from twisted.internet import defer
from twisted.python import log

from buildbot.changes.changes import Change
from buildbot.process.properties import Properties
from buildbot.process.results import CANCELLED
from buildbot.process.results import EXCEPTION
from buildbot.process.results import FAILURE
from buildbot.process.results import RETRY
from buildbot.process.results import SUCCESS
from buildbot.process.results import WARNINGS
from buildbot.process.results import statusToString
from buildbot.process.results import worst_status
from buildbot.reporters import utils
from buildbot.util import json
from buildbot.util import service
from buildbot.util.eventual import eventually
from buildbot.util.state import StateMixin
from buildbot.util.xml import XMLString

# exported for use by other modules
Results = [SUCCESS, WARNINGS, FAILURE, SKIPPED, EXCEPTION, RETRY, CANCELLED]
Results.extend(range(128, 256))
Results = tuple(Results)


