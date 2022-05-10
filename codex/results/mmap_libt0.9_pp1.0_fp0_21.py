import mmap
import sys
from datetime import datetime, timedelta

def get_dmax_from_census(s):
    lines = s.splitlines()

    dmax = []
    for line in lines:
        fields = line.split()

        # get time stamp and convert to milliseconds
        time_str = ' '.join(fields[1:4])
        dt_obj = datetime.strptime(time_str, "%a %b %d %H:%M:%S %Z %Y")
        dt_tms = int(dt_obj.timestamp() * 1000)

        # get the rest of the fields
        mem_free, mem_total, mem_cache, dmax_mb = fields[9:13]

        # dmax is the size of the file system cache
        dmax_kb = int(dmax_mb) * 1000

        # convert to milliseconds
        dmax_ms = int(dmax_kb / (mem_cache / 1000) / 1000)

        duple = (dt_tms, dmax_ms)
        dmax.
