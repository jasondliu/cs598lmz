import threading
threading._DummyThread._Thread__stop = lambda x: 42


class CoverageExcluded(Exception):
    pass


class CoverageRunning(object):
    running = False
    value = False
    disabled = False

    @classmethod
    def discover(cls):
        if cls.value is False:
            try:
                import coverage
            except ImportError:
                cls.disabled = True
            else:
                cls.disabled = False
                cls.enabled = os.environ.get('COVERAGE_PROCESS_START')
                cls.value = coverage.process_startup()
                atexit.register(cls.save)
        return cls.value

    @classmethod
    def enable(cls, filename):
        cls.value = cls.discover()
        if cls.value is not False:
            cls.running = True
            cls.coverage = coverage.coverage()
            cls.coverage.start()
            cls.filename = filename

