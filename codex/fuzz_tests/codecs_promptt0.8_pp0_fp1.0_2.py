import codecs
# Test codecs.register_error("calamari")

# ----- CRAWLER -----

class RandomAgent(Agent):
    """
    Agent that chooses random actions with uniform probability.
    """
    def __init__(self, observation_space, action_space):
        super(RandomAgent, self).__init__(observation_space, action_space)
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()


class Crawler2(Env):
    """
    OpenAI Gym environment for a crawling robot.

    A 4-joint crawler starts in a random configuration in the box [-1.5, 1.5]^3,
    and must crawl to the origin.
    """
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 50
    }

    def __init__(self):
        self.bounds = np.array([[-1.5, 1.5]] * 3)
        self.action_
