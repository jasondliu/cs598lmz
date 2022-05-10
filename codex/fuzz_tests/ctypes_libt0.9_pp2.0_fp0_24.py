import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
import matplotlib.pyplot as plt

from env import Env

def train(env, **kwargs):
    hid_size, lr, epochs, print_logs = map(
        kwargs.get, ['hid_size', 'lr', 'epochs', 'print_logs']
    )
    if print_logs: print(kwargs)
    net, opt, crt = create_net(env, hid_size=hid_size, lr=lr)
    for epoch in range(epochs):
        obs, actions, rewards, dones = [], [], [], []
        o, r, d, ep_r, ep_t = env.reset(), 0, False, 0, 0
        while not d:
            obs.append(o)
            a = net.choose_action(o)
            a = torch.tensor([a], dtype=torch.long, device=device)
            o_new, r, d, _ = env.
