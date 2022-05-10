import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    f = F()
    a.append(f)
    select.select(a, a, a)

class MyFile:
    def fileno(self):
        return 1

def test_select_mutated_with_instance():
    a = []
    f = MyFile()
    a.append(f)
    select.select(a, a, a)

class MyFile2:
    def fileno(self):
        return 1

def test_select_mutated_with_instance2():
    a = []
    f = MyFile2()
    a.append(f)
    select.select(a, a, a)

class MyFile3:
    def fileno(self):
        return 1

def test_select_mutated_with_instance3():
    a = []
    f = MyFile3()
    a.append(f)
    select.select(a, a, a)

class MyFile4:
    def fileno(self):
        return 1

