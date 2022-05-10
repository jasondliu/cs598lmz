import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

parser = argparse.ArgumentParser(description='Plotting the results of a CSV file.')
parser.add_argument('--csv-file', type=str, default="../logs/log", help='The CSV file to plot.')
parser.add_argument('--x-axis', type=str, default="epoch", help='The x-axis to plot on.')
parser.add_argument('--y-axis', type=str, default="val_acc", help='The y-axis to plot on.')
parser.add_argument('--title', type=str, default="", help='The title of the plot.')
parser.add_argument('--show', type=bool, default=True, help='Show the plot.')
parser.add_argument('--save-path', type=str, default="plot.png", help='Path to save the plot.')
args = parser.parse_args()

