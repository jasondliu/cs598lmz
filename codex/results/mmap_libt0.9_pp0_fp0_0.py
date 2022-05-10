import mmap

d = {}

config_list_file = "/home/aswamy/performance/scripts/analysis/perf/perf_config_list"
output_dir = '/home/aswamy/performance/output/perf/'

manual_workloads_file = "manual_workloads"

try:
    manual_workloads_data = open(manual_workloads_file, 'r')
except:
    print("ERROR: Unable to open: " + manual_workloads_file)
    exit(1)

for line in manual_workloads_data:
    if not line:
        continue

    (workload, is_manual) = line.split()

    #ignore is_manual for now
    d[workload] = None

#print(d)
#print(d.keys())

for workload in d:
    perf_config_file = next((f for f in os.listdir(output_dir + workload + '/') if f.endswith('.perf.config')), None)

    if perf_config_
