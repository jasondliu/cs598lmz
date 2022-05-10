import select
import os
import sys
import subprocess
import errno

from hwsim import HWSimRadio
from test_suite_80211 import exec_ll_ts

def get_next_ts_num(ts_num):
    if ts_num is None:
        return 1
    else:
        return ts_num + 1

hwsim = HWSimRadio()

# default values for test parameters
test_ts_num = None
test_func = None
test_mode = "master"
test_freq = None
test_chan = None
test_chans = None
test_chanset = None
test_duration = None
test_essid = None
test_bssid = None
test_int = None
test_sint = None
test_bint = None
test_retries = None
test_rts = None
test_frag = None
test_txop = None
test_tx = None
test_txpwr = None
test_ant = None
test_sgi = None
test_ldpc = None
test_stbc =
