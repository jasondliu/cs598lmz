import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Parse options
parser = argparse.ArgumentParser()
parser.add_argument('--game', help='Name of the game', default='Catcher')
parser.add_argument('--display',
                    dest='display',
                    action='store_true',
                    help='Display screen (default: False)')
parser.add_argument('--nodisplay',
                    dest='display',
                    action='store_false',
                    help='Do not display screen (default: False)')
parser.set_defaults(display=False)
parser.add_argument('--scale', help='Display scaling', default=None)
