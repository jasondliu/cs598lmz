import threading
threading.stack_size(2 ** 27)

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os


def create_thread(_func, _args, _name):
    _thread = threading.Thread(target=_func, args=_args, name=_name)
    _thread.daemon = True
    _thread.start()


def get_action(s):
    global g_PI

    prob = sess.run(g_PI, feed_dict={X: [s]})[0]

    action = np.random.choice(a_size, p=prob)
    return action


def discount_rewards(r):
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add
    return discounted_r


def step(ep
