import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    fd = F()
    a.append(fd)

    rfds, wfds, xfds = select.select([fd], [fd], [], 1)
    assert rfds == []
    assert wfds == []
    assert xfds == []

if __name__ == '__main__':
    import pytest
    pytest.main(str(__file__))
