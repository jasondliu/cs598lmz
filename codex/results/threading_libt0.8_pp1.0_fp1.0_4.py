import threading
threading.LOCK_SIZE = 1024 * 8

import threading
threading.stack_size(2 * 1024 * 1024)


def initABAG(args):
    abag = ABAG(args)
    return abag


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', default=0, type=int, help='random seed')
    parser.add_argument('--hidden_size', default=128, type=int)
    parser.add_argument('--count_expert_size', default=50, type=int)
    parser.add_argument('--use_expert', default=1, type=int)
    parser.add_argument('--num_workers', default=8, type=int)
    parser.add_argument('--gamma', default=0.99, type=float)
    parser.add_argument('--tau', default=5e-3, type=float)
    parser.add_argument('--lr_actor', default=3e-4, type=float)
