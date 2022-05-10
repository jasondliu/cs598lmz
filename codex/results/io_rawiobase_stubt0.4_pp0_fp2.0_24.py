import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

def get_input(day):
    return File(open('input/day{}.txt'.format(day), 'r'))

def get_output(day, part):
    return File(open('output/day{}-{}.txt'.format(day, part), 'w'))

def get_day(day):
    with open('input/day{}.txt'.format(day), 'r') as f:
        return f.read().splitlines()

def get_day_as_list(day):
    return [list(l) for l in get_day(day)]

def get_day_as_list_of_lists(day):
    return [list(map(int, l.split())) for l in get_day(day)]
