import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

from sklearn.preprocessing import MinMaxScaler

from lab import *
from lab.envs.mujoco import *
from lab.envs.mujoco.walker2d import Walker2dEnv

from lab_extensions.envs.mujoco.walker2d_black import Walker2dEnvBlack
from lab_extensions.envs.mujoco.walker2d_imitation_learning_env import Walker2dImitationLearningEnv

from NNInput import *
from ReplayMemory import *


#################################################################################################
# This code is to implement Deep Deterministic Policy Gradient 
#################################################################################################
def run(env, n_episodes, reward_to_stop, test_name, load_pretrained, model_path='./pretrained/'):

    #################################################################################################
    # prepare env
    #################################################################################################
    ob_space = env.observation_space
    ac_space = env.action_space

    print("ob_space: ", ob_space)
    print
