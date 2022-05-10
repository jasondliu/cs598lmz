import types
types.ClassType = type # py3 compat

# This only works for system-installed python packages
import distro
import distro.subscribers
import distro.spa

from distro.subscribers import Pkgsubscriber, Appsubscriber, SessionMonitor, \
    ConfigSubscriber
from GUB.Tools.macros import package

distro.subscribers.Pkgsubscriber = Pkgsubscriber
distro.subscribers.Appsubscriber = Appsubscriber
distro.subscribers.SessionMonitor = SessionMonitor
distro.subscribers.ConfigSubscriber = ConfigSubscriber

from GUB.Tools.mutators import PathSourceMutator, NewPkgLogMutator
def spa_init (self):
    if self.mirror_host:
        self.archive_urls = self.mirror_host.split (' ')
    else:
        self.archive_urls = []
    self.package_suites = self.package_suites.replace (' ','')

    spa_init._initialize (self)

