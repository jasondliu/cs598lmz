fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = mock.Mock()
gi.gi_frame = mock.Mock(f_code=fn.__code__)
gi.gi_running = False

frame = mock.Mock()
frame.f_globals = {'__file__': __file__}
frame.f_lasti = -1
frame.f_lineno = 1

frame.f_code = fn.__code__
gi.gi_frame = frame

code = mock.Mock(co_firstlineno=frame.f_lineno)
code.co_filename = frame.f_code.co_filename = __file__

diff.diff_string = lambda a, b, fromfile, tofile: 'diff_string'


@pytest.fixture
def mock_get_frame_info(monkeypatch):
    mock_info = mock.Mock(source='code')
    monkeypatch.setattr('xonsh.inspectors.getframeinfo', mock_info)


@pytest.fixture
def mock_get_code(monkeypatch):
