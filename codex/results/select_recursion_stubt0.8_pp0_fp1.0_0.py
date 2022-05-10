import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self.x)

    def prep(x):
        f = F()
        f.x = x
        return f

    fds = [prep(0), prep(1), prep(2), prep(3), prep(4), prep(5),
           prep(6), prep(7), prep(8), prep(9)]

    select.select(fds, [], [])
    assert a == list(range(10))

class myfile:
    def __init__(self, name, content):
        self.file = open(name, 'w')
        self.name = name
        self.content = content
    def fileno(self):
        return self.file.fileno()
    def __del__(self):
        self.file.write(self.content)
        self.file.close()
        os.unlink(self.name)

def test_select_with_deleted_fd():
    fd = myfile(str(udir.join('select_deleted')), 'y')
    assert select.select([
