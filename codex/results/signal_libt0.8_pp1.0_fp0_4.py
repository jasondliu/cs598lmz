import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # enable ctrl-c

if __name__ == "__main__":

	# Load data
	# state_dim = env.get_state_dim()
	# action_dim = env.get_action_dim()
	state_dim, action_dim = env.dim()
	env_name = env.get_name()
	print("ENVIRONMENT NAME: ", env_name)
	assert(env_name != None)
	print("state size: ", state_dim)
	print("action size: ", action_dim)
	# Load configs and setup results folder
	configs = json.load(open("configs.json", "r"))
	if configs["save_results"]:
		time_id = datetime.now().strftime("_%Y_%m_%d_%H_%M_%S")
		results_path = configs["results_directory"]+"/"+env_name+time_id+"/"
		os.
