import gc, weakref

from twisted.internet import defer, reactor
from twisted.python import log

from buildbot import config
from buildbot.process import buildstep, logobserver, properties
from buildbot.process.buildstep import SUCCESS, FAILURE, EXCEPTION, SKIPPED, BuildStep
from buildbot.process.properties import Properties
from buildbot.status.results import SUCCESS, WARNINGS, FAILURE, SKIPPED, EXCEPTION
from buildbot.steps.source import Source
from buildbot.steps.shell import ShellCommand
from buildbot.steps.transfer import FileUpload

class BuildFactory(object):
    """I implement a BuildFactory, which generates Builds and their
    Steps. Each Build has a factory, which generates a new Build with
    fresh Steps each time a Build is needed.

    @type  buildClass: L{buildbot.process.build.Build}
    @ivar  buildClass: the class to use when creating new Builds. This
                       should be a subclass of buildbot.process.build.Build.

    @type  properties: dictionary
    @ivar 
