import lzma
lzma.LZMA_OK

# some native modules are not available on all platforms
# so we need to disable some tests.
# see https://github.com/pybee/toga/issues/13

# from toga.platforms.gtk import GTK
# from toga.platforms.winforms import WinForms

# for now, we only test the gtk platform

TEST_PLATFORM = 'GTK'


@pytest.fixture(scope='session')
def toga_impl():
    if TEST_PLATFORM == 'GTK':
        from toga.platforms.gtk import GTK
        return GTK
    elif TEST_PLATFORM == 'WinForms':
        from toga.platforms.winforms import WinForms
        return WinForms
    else:
        raise RuntimeError('Unknown TEST_PLATFORM')


@pytest.fixture
def toga_app(toga_impl):
    return toga_impl.App('Test App', 'org.pybee.helloworld')


@py
