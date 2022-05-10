import codecs
# Test codecs.register_error()

import lib2to3.pytree
import six

@pytest.fixture()
def tmp_dir(tmpdir):
    return six.text_type(tmpdir.dirname)

@pytest.fixture()
def use_dir(tmpdir):
    os.chdir(six.text_type(tmpdir.dirname))

@pytest.fixture()
def rootdir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture()
def root_dir(tmpdir):
    root_dir = six.text_type(tmpdir.dirname)
    os.chdir(root_dir)
    file_list = {'glob_file.py':
                    '''# -*- encoding: utf-8 -*-
# test files for glob / unicode
def динозавр():
     print("Странное завещание")
    ''
