import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    o = F()
    a = [1,2]
    fd_set, read_fd_set, write_fd_set, exec_fd_set = select.select([o], [o], [o], 1)
    assert fd_set == read_fd_set == write_fd_set == exec_fd_set == []

def test_parse_select_result():
    assert select.parse_select_result([], [], [], 'abc') == 'abc'
    py.test.raises(ValueError, select.parse_select_result, [], [], [], 'ab')
    py.test.raises(ValueError, select.parse_select_result, [], [], [], 'abcd')
    assert select.parse_select_result([0], [], [], '\x00') == 0
    assert select.parse_select_result([0], [], [], '\x01') == 1
    assert select.parse_select_result([0], [], [], '\xff') == 255
    assert
