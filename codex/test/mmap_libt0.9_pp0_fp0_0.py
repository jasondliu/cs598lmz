import mmap

d = {}

config_list_file = "/home/aswamy/performance/scripts/analysis/perf/perf_config_list"
output_dir = '/home/aswamy/performance/output/perf/'

manual_workloads_file = "manual_workloads"

try:
    manual_workloads_data = open(manual_workloads_file, 'r')
except:
    print("ERROR: Unable to open: " + manual_workloads_file)
