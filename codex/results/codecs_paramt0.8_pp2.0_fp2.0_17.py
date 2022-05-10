import codecs
codecs.register_error("strict", codecs.replace_errors)
import collections

class Log(object):
    def __init__(self, file_name):
        self.log = []
        self.writers = {}
        self.file_name = file_name
        self.current_line = 0

    def append(self, line, **kwargs):
        self.log.append((line, kwargs))
        self.current_line += 1
        for writer in self.writers.values():
            writer.write(line, **kwargs)

    def add_writer(self, writer):
        self.writers[writer.name] = writer

    def remove_writer(self, writer):
        del self.writers[writer.name]

    def save(self):
        with open(self.file_name, "w") as f:
            for line in self.log:
                f.write(line[0])
                f.write("\n")


class LogWriter(object):
    def __init__(self, name):
        self.name = name

    def write(self
