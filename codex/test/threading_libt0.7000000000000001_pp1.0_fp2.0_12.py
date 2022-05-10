import threading
threading.stack_size(65536)


class Thread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)

    def run(self):
        self._target(*self._args)

# External call
def start_new_thread(function, args):
    Thread(target=function, args=args).start()

def main():
    # do something in main thread
    pass

if __name__ == "__main__":
    main()
