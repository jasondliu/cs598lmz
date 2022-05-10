import _struct as struct
from struct import error as struct_error

import third_party.pcap as pcap

import net_common

if os.path.basename(__file__).startswith('pcap_'):
	net_common.module_name = 'network.device.' + \
		os.path.basename(__file__)[5:-3]

if os.path.basename(__file__).startswith('pcap_tcp'):
	net_common.module_config_name = \
		net_common.module_config_name.replace('tcp_', 'ethernet_')

import net_logging

##### Public constants #####

LOOP_INFINITE = -1

### Protocol constants ###

ETH_P_IP = getattr(pcap, 'ETH_P_IP', 0x0800)
ETH_P_IPV6 = getattr(pcap, 'ETH_P_IPV6', 0x86DD)

ETH_TYPE_CODES = {
	ETH_P_IP:
