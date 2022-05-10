import select


class Process(object):
    @classmethod
    def call(cls, *args, **kwargs):
        if kwargs.get('shell', False):
            args = [args[0]]
        p = subprocess.Popen(args, **kwargs)
        p.wait()
        return p.returncode

    @classmethod
    def call_expect(cls, expect, *args, **kwargs):
        if kwargs.get('shell', False):
            args = [args[0]]
        p = subprocess.Popen(args, **kwargs)
        output = []
        while p.returncode is None:
            p.poll()
            if p.stdout:
                for line in iter(p.stdout.readline, b''):
                    output.append(line)
                    if expect in line:
                        p.stdout.close()
                        return
        raise Exception('not find expect.')

    @classmethod
    def call_timeout(cls, timeout, *args, **kwargs):
        if kwargs
