import ctypes
ctypes.cast(v, ctypes.py_object).value

total_time = 0
n_steps = 0
while not done:
    display_time = time.time()
    # RL choose action based on observation
    action = RL.choose_action(observation)

    # RL take action and get next observation and reward
    observation_, reward, done = env.step(action)

    RL.store_transition(observation, action, reward, observation_)

    if (step > 200) and (step % 5 == 0):
        RL.learn()

    # swap observation
    observation = observation_

    # break while loop when end of this episode
    if done:
        break
    step += 1
    total_time += time.time() - display_time
    n_steps += 1

print('steps={}, average display time={}'.format(n_steps, total_time/n_steps))
