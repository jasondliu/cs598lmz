import threading
# Test threading daemon
#test_daemon = threading.Thread(target=test_thread, args=(1, ), name="producer")
#test_daemon.setDaemon(True)


try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Welcome to the optimizer.")

    parser.add_argument("--num_workers", "-wn", type=int)
    parser.add_argument("--max_runs", "-nr", default=10, type=int)
    parser.add_argument("--max_steps", "-ns", default=15, type=int)
    parser.add_argument("--min_loss", "-ml", default=0.05, ty
