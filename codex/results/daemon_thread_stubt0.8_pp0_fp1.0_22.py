import sys, threading

def run():
    args = []
    for arg in sys.argv[1:]:
        args.append(arg)
    threading.Timer(3.0, run).start()
    os.chdir("/home/vaibhav/Documents/projects/hacks/gamepad_stream")
    os.system("python gamepad_stream.py" + " " + " ".join(args))

def main():
    run()

if __name__ == '__main__':
    main()
