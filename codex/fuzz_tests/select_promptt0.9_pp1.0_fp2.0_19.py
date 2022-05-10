import select
# Test select.select, this is not documented and does not even exist with
# socket.SOCK_DGRAM
assert select.select([], [], [], 0) == ([], [], []), "select.select fails"

# Sanitize OS environment
for key in list(os.environ.keys()):
    if key.find('STX') == 0:
        del os.environ[key]

#
# Setup testing environment
#
import unittest
import subprocess
import tempfile

os.environ['CC'] = 'gcc'
os.environ['CXX'] = 'g++'
os.environ['FC'] = 'gfortran'
os.environ['bin_dir'] = '/usr/bin'
os.chdir(tempfile.mkdtemp(prefix=os.environ['user'] + '-stx-test-'))
os.environ['BUILD_PREFIX'] = os.getcwd()
os.environ['PATH'] = os.path.join(os.getcwd(), 'bin') + ':' + os.en
