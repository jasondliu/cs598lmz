import types
types.ModuleType.__getattr__ = getattr


def run():
    import sys
    from IPython.utils.syspathcontext import prepended_to_syspath
    from IPython.core.shellapp import run_ipython

    with prepended_to_syspath(os.path.abspath('.')):
        status = run_ipython(sys.argv)
        sys.exit(status)


def install():
    from setuptools import setup
    from setuptools.command.develop import develop
    from setuptools.command.install import install

    class RunInstall(object):
        def __init__(self, install_func):
            self.install_func = install_func

        def __call__(self, *args, **kwargs):
            with open('requirements.txt') as requirements:
                for line in requirements:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        install_requires.append(line)
            self.install_func(*args, **kwargs)

    def install_ip
