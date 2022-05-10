import socket
# Test socket.if_indextoname function
#
# If network device is not up, interface index cann't be resolved by
# if_indextoname(). The failure is unexpected.
#
# Author: Honghui Lai <laihh@cn.ibm.com>
# Date:  2007-03-08
#
# Bug reference:
# http://www.linux-foundation.org/bugzilla/show_bug.cgi?id=1564 

NUM_TEST = 31

import common
from autotest_lib.client.bin import utils

cmd = 'ifconfig -a|grep lo:|sed "s/.*lo: \(.*\)> mtu.*/\\1/g"'
(rc, interface) = utils.run(cmd, ignore_status=True)
if interface:
    interface_index = socket.if_nametoindex(interface)
