import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

def get_arguments():
    parser = argparse.ArgumentParser(description='Calculate the average of the first column of a file')
    parser.add_argument('-i', '--infile', type=str, nargs='?', help='infile')
    parser.add_argument('-o', '--outfile', type=str, nargs='?', help='outfile')
    return parser.parse_args()

def main():
    args = get_arguments()
    infile = open(args.infile, 'r')
    outfile = open(args.outfile, 'w')
    numbers = []
    for line in infile:
        numbers.append(float(line.split()[0]))
    average = np.mean(numbers)
    stdev = np.std(numbers)
    outfile.write(str(average) + ' ' + str(stdev))

if __name__ == '__main__':
    main
