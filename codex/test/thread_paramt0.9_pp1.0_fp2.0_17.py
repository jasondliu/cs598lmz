import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

############################# GLOBALS ################################
# Actions
number_of_actions = 7
actions_list = ["NOOP", "FIRE", "UP", "RIGHT", "LEFT", "DOWN", "UPRIGHT", "UPLEFT", "DOWNRIGHT", "DOWNLEFT"]
actions_dict = {actions_list[i]: i for i in range(len(actions_list))}

# Parameters
clipping_rewards = True
max_global_steps = 3000
gamma = 0.99  # Discount factor
batch_size = 32
eval_freq = 300  # validate every 300 episodes
save_freq = 300  # save every 300 episodes
report_freq = 10
record_freq = 2
buffer_size = 500000
eval_episodes = 50

# SOSBAN Training Parameters
trials_number = 10
beta = 0.05

########################### UTILS FUNCTIONS ####################################
