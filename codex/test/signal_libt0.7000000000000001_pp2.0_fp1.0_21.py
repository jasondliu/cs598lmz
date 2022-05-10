import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

n_steps = 3

def _parse_args():
	parser = argparse.ArgumentParser(
		description="Generate a random number and print to stdout"
	)
	parser.add_argument(
		'--mean', '-m',
		default=0,
		type=float,
		help='The mean of the distribution of numbers'
	)
	parser.add_argument(
		'--stddev', '-s',
		default=1,
		type=float,
		help='The standard deviation of the numbers'
	)
	parser.add_argument(
		'--repeat', '-r',
		default=None,
		type=int,
		help='Number of times to repeat (default: one-shot)'
	)
	return parser.parse_args()

def main():
	args = _parse_args()
