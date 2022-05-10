import sys, threading

def run():
    args = sys.argv
    loader = Loader()
    loader.load(args[0])
    if len(args) > 1:
        loader.load(args[1])
    time.sleep(2)
    loader.unload(args[0])
    if len(args) > 1:
        loader.unload(args[1])

if __name__ == "__main__":
    run()
