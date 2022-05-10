import io
class File(io.RawIOBase):
    def writable(self):
        return True
    def write(self):
        print "File.write(): doing nothing"

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
    reports = yield
    rep = reports.pop()

    # print rep
    # print rep.outlines
    # print rep.sections
    # print rep.longrepr
    # print rep.longrepr.reprcrash
    # print rep.longrepr.reprtraceback
    # print dir(rep.longrepr)
    # print rep.longrepr._excinfo
    # print rep.longrepr._excinfo[2]
    # print dir(rep.longrepr._excinfo[2])
    # print rep.longrepr._excinfo[2].tb_next
    # print rep.longrepr._excinfo[2].tb_frame
    # print rep.longrepr._excinfo[2].tb_lineno
    # print rep.
