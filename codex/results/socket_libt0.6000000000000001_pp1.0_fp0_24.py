import socket

from ipmininet.clean import cleanup
from ipmininet.ipnet import IPNet
from ipmininet.iptopo import IPTopo
from ipmininet.router.config import RouterConfig, ebpf_text, eBPFProgram
from ipmininet.router.config.ebpf import eBPFRegisters
from ipmininet.router.config.zebra import Zebra, ZebraRoute
from ipmininet.tests.utils import assert_connectivity
from . import require_root


class DummyRouterConfig(RouterConfig):

    def build(self, *args, **kwargs):
        self.addDaemon(Zebra, reload_config=True,
                       config_format='json', config_file='/etc/zebra.json')


class eBPFTopo(IPTopo):

    def build(self, *args, **kwargs):
        r1 = self.addRouter('r1', use_v4=True, use_v6=False,
                            config=DummyRouterConfig)
        r2 = self
