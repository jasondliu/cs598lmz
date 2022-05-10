import signal
signal.signal(signal.SIGINT, signal_handler)

import sys

# TODO:
#   - Add support for multiple GPUs
#   - Add support for multiple processes
#   - Add support for multiple environments

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logdir', default='results/logs',
                        help='Log directory [results/logs]')
    parser.add_argument('--env', default='BreakoutDeterministic-v4',
                        help='Environment name [BreakoutDeterministic-v4]')
    parser.add_argument('--gpu', default=0, type=int,
                        help='GPU to use [0]')
    parser.add_argument('--num-envs', default=8, type=int,
                        help='Number of environments [8]')
