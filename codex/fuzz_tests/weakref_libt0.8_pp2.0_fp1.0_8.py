import weakref

from twisted.internet.task import LoopingCall
from twisted.internet.defer import inlineCallbacks, returnValue, succeed

from ..web.root import RootResource
from .base import IModule, ModuleBase
from .interfaces import IModuleContent, IModuleInstaller
from .resource import ModuleStaticResource
from ..utils.module import load_module


class ModuleInstaller(object):

    implements(IModuleInstaller)

    finder_type = 'file'
    finder_resources = ()
    finder_title = 'Files'

    def __init__(self, module_manager, module_jobs, confman):
        self.module_manager = module_manager
        self.module_jobs = module_jobs
        self.confman = confman

    def install(self, module_id, install_from):
        if install_from.endswith('.py') or install_from.endswith('.xpy'):
            self._installPythonModule(module_id, install_from)
        else:
            self._installBundle(module_id, install
