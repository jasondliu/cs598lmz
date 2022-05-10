import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
'''

SANDBOX_PROGRAM = '''

class sandbox_client(object):
    def __init__(self):
        self.get = self.sand_get
        self.post = self.sand_post

    def main(self, env, start_response):
        if env['REQUEST_METHOD'] == 'GET':
            return self.get(env, start_response)
        elif env['REQUEST_METHOD'] == 'POST':
            return self.post(env, start_response)

    def sand_get(self, env, start_response):
        start_response('200 OK', [])
        return [b'Hello World']

    def sand_post(self, env, start_response):
        start_response('200 OK', [])
        return [env['wsgi.input'].read()]

application = sandbox_client().main
'''


def write_to_package(package_path, content, import_name=None):
    library_path = os.path.realpath(os.path.join(package_path, '
