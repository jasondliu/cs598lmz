import types
types.ModuleType.__repr__ = lambda self: self.__name__

def test_import_all():
    from pytest_mock import mocker
    mocker.patch('pytest_mock.mocker.MockFixture.__init__', lambda self, *args, **kwargs: None)
    mocker.patch('pytest_mock.mocker.MockFixture.start', lambda self: None)
    mocker.patch('pytest_mock.mocker.MockFixture.stop', lambda self: None)
    mocker.patch('pytest_mock.mocker.MockFixture.get_autospec', lambda self, *args, **kwargs: None)
    mocker.patch('pytest_mock.mocker.MockFixture.get_spec', lambda self, *args, **kwargs: None)
    mocker.patch('pytest_mock.mocker.MockFixture.get_spec_set', lambda self, *args, **kwargs: None)
    mocker.patch('pytest_m
