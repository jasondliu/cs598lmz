import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            
    def _():
        a.append(1)
    
    r = select.select([F()], [], [], 0.5)
    print 'returned', r
    print 'len', len(a)
    assert len(a) < 100
    

if __name__ == '__main__':
    test_select_mutated()
