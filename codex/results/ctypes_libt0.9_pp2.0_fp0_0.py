import ctypes
ctypes.windll.shell32.IsUserAnAdmin() ### Do we have admin rights?

try:
    #### Maybe there is a better place for the config file (e.g. .decomp? or .decomp/config, .decomp/log?)
    config_file = open('decomp_config.cfg', 'r')
    config_lines = config_file.read().splitlines()
    for line in config_lines:
        if 'tag_path' in line:
            tag_path = line.split('=')[1]
        elif 'log' in line:
            log = line.split('=')[1]
        elif 'last_log' in line:
            last_log = line.split('=')[1]
    config_file.close()

    if log == 'yes': # open new log file
        now = datetime.datetime.now()
        #log_path = 'decomp.log'
        log_path = 'decomp_' + now.strftime("%Y_%m_%d_%H_%M_%
