import threading
threading.stack_size(1024*1024)

class Watcher():
    def __init__(self, watch_dir, handle_func, recursive=True):
        self.watch_dir = watch_dir
        self.handle_func = handle_func
        self.recursive = recursive
        self.observer = Observer()

    def run(self):
        event_handler = Handler(self.handle_func, self.recursive)
        self.observer.schedule(event_handler, self.watch_dir, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Watcher stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self, func, recursive):
        super(Handler, self).__init__()
        self.func = func
        self.recursive = recursive

    def on_created(self, event):
        if not event.is_directory:
