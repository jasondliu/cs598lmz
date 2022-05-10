import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append('fileno')
            return 1
        def read(self):
            test_select_mutated()
            a.append('read')
            return 'Test'
        def close(self):
            test_select_mutated()
            a.append('close')

    class G:
        def fileno(self):
            test_select_mutated()
            a.append('fileno')
            return 2
        def write(self):
            test_select_mutated()
            a.append('write')
            return 5
        def close(self):
            test_select_mutated()
            a.append('close')

    class H:
        def fileno(self):
            test_select_mutated()
            a.append('fileno')
            return 1
        def write(self):
            test_select_mutated()
            a.append('write')
            return 5
        def close(self):
            test_select_mutated()
            a.append('close')

    f = F()
    g = G()
   
