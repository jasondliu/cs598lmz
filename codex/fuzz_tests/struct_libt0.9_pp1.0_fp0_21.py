import _struct
from extras import Encoder
import json
from collections import OrderedDict as OD
import bz2file as bz2

def initialize():
    global cache, config, f_perf, f_perf_all, f_sched, f_sched_all, sched_f, sched_b, sched_n, config_f, config_b, config_n, perf_f, perf_b, perf_n, quick_f, quick_b

    cache = {}
    config = {}

    header_schema = [(k, int) for k in ['pid', 'uid', 'gid', 'tgid', 'time', 'inserted', 'lost']]
    header_schema +=] [(k, float) for k in [
            'prev_time', 'energy', 'cycles', 'elapsed_delta', 'elapsed_acc', 'perf_backtrace'
            ]]
    header_schema += [(k, str) for k in ['comm', 'name', 'cmdline', 'trace']]

    perf_schema = header_schema + [(k
