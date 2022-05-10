import codecs
codecs.register_error("strict", codecs.replace_errors)

try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess
        errno = subprocess.call([sys.executable, "runtests.py"])
        raise SystemExit(errno)

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    os.system("python setup.py bdist_egg upload")
    sys.exit()

# Get the long description from the README file
with codecs.open(os.path.join(here, "README.rst"), encoding="utf-8",
                 errors="strict") as fp:
    long_description = fp
