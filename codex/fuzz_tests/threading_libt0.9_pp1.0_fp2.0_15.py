import threading
threading.stack_size(67108864)
class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def start(self, name, task):
        self.busy = True
        display(HTML('<h4>{}</h4>'.format(name)))
        threading.Thread(target=task).start()
        threading.Thread(target=self.spinner_task).start()

    def stop(
