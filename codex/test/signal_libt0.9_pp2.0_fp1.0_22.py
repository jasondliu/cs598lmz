import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

if not os.path.exists(wd+'/Results'):
	os.makedirs(wd+'/Results')

if not os.path.exists(wd+'/Results/Track'):
	os.makedirs(wd+'/Results/Track')

if not os.path.exists(wd+'/Results/Traj'):
	os.makedirs(wd+'/Results/Traj')

if not os.path.exists(wd+'/Variables'):
	os.makedirs(wd+'/Variables')

if not os.path.exists(wd+'/Variables/Traj'):
	os.makedirs(wd+'/Variables/Traj')

if not os.path.exists(wd+'/Variables/Track'):
	os.makedirs(wd+'/Variables/Track')


input_files = sorted(glob.glob(input_file_name+'*'))
