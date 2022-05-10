import threading
threading.stack_size(67108864)
'''
Loads configuration from two JSON files:
./master.json
./local.json (not committed to repo)
'''
try:
    f = open('./master.json', 'r')
    master = json.load(f)
    f.close()

    # load values from master
    if 'hostname' in master:
        hostname = master['hostname']
    if 'port' in master:
        port = master['port']
    if 'no_of_workers' in master:
        no_of_workers = master['no_of_workers']
    if 'queue_size' in master:
        queue_size = master['queue_size']
    if 'camera_width' in master:
        camera_width = master['camera_width']
    if 'camera_height' in master:
        camera_height = master['camera_height']
    if 'frame_limit' in master:
        frame_limit = master['frame_limit']
    if 'logging_interval_s' in master:
