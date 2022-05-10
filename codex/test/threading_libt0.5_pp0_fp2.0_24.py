import threading
threading.stack_size(100000000000000)

# define a function to run the code on the worker threads
def worker(num):
    # create a session for each worker
    with tf.Session(config=config) as sess:
        # set up the environment for each worker
        env = gym.make('CartPole-v0')
        env.seed(0)
        np.random.seed(0)
        tf.set_random_seed(0)

        # set up the agent
        agent = Agent(sess,
                      state_size=4,
                      action_size=2,
                      learning_rate=0.00025,
                      epsilon=1.0,
                      epsilon_decay=0.9999,
                      epsilon_min=0.1,
                      gamma=0.99)

        # run the simulation for the specified number of episodes
        for episode in range(num_episodes):
            # reset the environment for each episode
            state = env.reset()
            state = np.reshape(state, [1, 4])
            reward_
