import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(data[0]))).start()

def main(args):
    if args.action == 'gen':
        gen(args)
    elif args.action == 'plot':
        plot(args)

def gen(args):
    # Read the data file
    data = []
    with open(args.data) as f:
        for line in f:
            data.append(line.strip().split('\t'))
    # Initialize the generator
    gen = Generator(
        data,
        args.out,
        n_frames=args.n_frames,
        footprint=args.footprint,
        size=args.size,
        offset=args.offset,
        fps=args.fps,
        duration=args.duration
    )
    # Generate the frames
    gen.run()

def plot(args):
    # Read the data file
    data = []
