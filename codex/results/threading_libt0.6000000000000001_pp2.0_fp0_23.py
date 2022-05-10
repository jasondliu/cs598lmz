import threading
threading.stack_size(2**27)

# Setup the environment
import gym
env = gym.make('CartPole-v0')
env.reset()

# Define the agent
class agent(object):
    
    def __init__(self):
        self.action_size = env.action_space.n
        self.state_size = env.observation_space.shape[0]
        self.gamma = 0.99
        self.epsilon = 0.05
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._create_model()
        self.model_target = self._create_model()
        self.update_target_weights()
        
    def _create_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))

