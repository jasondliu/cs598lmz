import lzma
lzma.LZMAError



class AdminImporter:

    def __init__(self, admin_config):
        self.admin_config = admin_config

    def download(self):

        req = urllib.request.Request(self.admin_config['url'])
        with urllib.request.urlopen(req) as response:
            self.data = response.read()

        self.fname = os.path.join(self.admin_config['temp_path'], self.admin_config['fname'])
        with open(self.fname, mode='wb') as f:
            f.write(self.data)

    def unpack(self):

        self.fname_lzma = self.fname + '.lzma'
        with open(self.fname, mode='rb') as f:
            with open(self.fname_lzma, mode='wb') as f_lzma:
                f_lzma.write(f.read())

        with open(self.fname_lzma, mode='
