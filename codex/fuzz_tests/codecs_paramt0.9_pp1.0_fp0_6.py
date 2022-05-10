import codecs
codecs.register_error('strict', codecs.ignore_errors)

class StdOutHandler():
    def log_event(self, event):
        print(event.as_dict_str())

class StdErrHandler():
    def log_event(self, event):
        print(event.as_dict_str(), file=sys.stderr)

class FileHandler():
    def __init__(self, filename, level):
        self.filename = filename
        self.level = level
        self.logfile = None

    def open_file(self):
        self.logfile = open(self.filename, 'a+')

    def log_event(self, event):
        if self.logfile is None:
            self.open_file()
        self.logfile.write(event.as_dict_byte() + b'\n')
        self.logfile.flush()

    def close(self):
        if self.logfile is not None:
            self.logfile.close()
        self.logfile = None


class Logger():
    def __init
