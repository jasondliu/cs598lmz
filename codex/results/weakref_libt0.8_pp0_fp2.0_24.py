import weakref
import sys

__all__ = ['Build']


class Build:
    def __init__(self, conf, cache, modeldir, testedir,
                 modelname=None, testname=None):
        if modelname is None:
            modelname = os.path.basename(modeldir)
        if testname is None:
            testname = os.path.basename(testedir)
        self.conf = conf
        self.cache = cache
        self.modeldir = os.path.realpath(modeldir)
        self.testedir = os.path.realpath(testedir)
        self.modelname = modelname
        self.testname = testname
        self.modelcommit = None
        self.testcommit = None
        self.scenarios = []

    def scenarionames(self):
        return [s.name for s in self.scenarios]

    def addscenario(self, name):
        if name in self.scenarionames():
            return
        klass = scenario.scenarios[name]
