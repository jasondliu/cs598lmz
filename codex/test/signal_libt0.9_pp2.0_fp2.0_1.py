import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

class createVirtualEnv(LocalBaseTask):
    """
    Create a virtual environment.
    """
    name = 'Create Virtual Environment'
    prjShareDir = luigi.Parameter(default=None)
    python = luigi.Parameter(default = 'python3.6')

    def run(self):
        venv = os.path.join(self.prjShareDir, 'venv')
        if not os.path.exists(venv):
            self.runCommandLine('virtualenv -p {p} {v}'.format(p=self.python, v=venv))
        self.setLocalOutputFiles()
        pass

class sampleOVL(LocalBaseTask):
    """
    Sample the .ovl file and place in the .input folder.
    """
    targetDir = luigi.Parameter(default=None)
    prjShareDir = luigi.Parameter(default=None)
    ovlFastaFilename = luigi.Parameter
