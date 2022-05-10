import weakref
import logging
import threading

from qubes.vm.qubesvm import QubesVM
from qubes.vm.templatevm import TemplateVM
from qubes.vm.adminvm import AdminVM
from qubes.vm import net
from qubes.vm.net import NetVMMixin
from qubes.vm.mix.net import NetVM
from qubes.vm.mix.net import DefaultNetVM
from qubes.vm.mix.net import NetVM as VMNetVM
from qubes.vm.mix.net import NetVM as ProxyNetVM
from qubes.vm.mix.net import NetVM as AppVMNetVM
from qubes.vm.mix.net import NetVM as StandaloneNetVM
from qubes.vm.mix.net import NetVM as NetVMMixinNetVM
from qubes.vm.qubesvm import QubesVM as NetVMMixinQubesVM
