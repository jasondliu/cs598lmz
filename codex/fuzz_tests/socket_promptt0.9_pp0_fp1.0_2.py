import socket
# Test socket.if_indextoname() on an unknown index
fromsocket = socket.fromfd = Mock(side_effect=OSError(errno.ENODEV, ""))

from ryu.lib.ifaces import if_indextoname

from mock import patch, Mock
from ryu.lib import hub
from ryu.topology.switches import LLDPPacket
from ryu.utils import binary_str
from ryu.services.protocols.ovsdb import ovs_vsctl
from ryu.services.protocols.ovsdb import table


class GetPortNameByIfIndex(unittest.TestCase):
    """Test get_port_name_by_ifindex() function.
    """

    @patch('ryu.lib.ifaces.fromfd')
    @patch('ryu.lib.ifaces.if_indextoname')
    def test_ifindex_int(self, if_indextoname, fromfd):
        # Test for ifindex = 1, then 2.
        # ifindex_1__name_None - We expect indextoname to fail, that is
