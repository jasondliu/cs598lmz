from lzma import LZMADecompressor
LZMADecompressor().decompress(comp_data)

#minizinc
from mzn import run_minizinc
run_minizinc(model_file, data_file)

#psutil
import psutil
psutil.cpu_count()
psutil.cpu_count(logical=False) # physical cores
psutil.cpu_stats()
psutil.cpu_percent(interval=0.5) # percent of cpu usage
psutil.cpu_times_percent()
psutil.virtual_memory()
psutil.swap_memory()
psutil.disk_partitions()
psutil.disk_usage('/')
psutil.disk_io_counters()
psutil.net_io_counters()
psutil.net_if_addrs()
psutil.net_if_stats()
psutil.sensors_temperatures()
psutil.sensors_fans()
psutil.sensors_battery()
psutil.boot_time()
psutil.pids()
psutil.Process(1)  # init
p.name()

