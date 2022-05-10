import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

from slivka import Service


class HashService(Service):
    def run(self):
        for line in sys.stdin:
            line = line.strip().decode('utf-8')
            if not line:
                break
            filename, url = line.split()
            content = self.get(url)
            with self.get_file(filename) as f:
                f.write(content)
            sys.stderr.write('{0}\n'.format(filename))
            sys.stderr.flush()


if __name__ == '__main__':
    HashService(port=int(sys.argv[1]))
