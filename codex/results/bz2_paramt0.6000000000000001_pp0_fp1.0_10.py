from bz2 import BZ2Decompressor
BZ2Decompressor = pycurl.Curl()

class Downloader:

    def __init__(self, url, file_name):
        self.url = url
        self.file_name = file_name

    def download(self):
        print("Downloading file:%s" % self.file_name)
        fp = open(self.file_name, "wb")
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, self.url)
        curl.setopt(pycurl.WRITEDATA, fp)
        curl.perform()
        curl.close()
        fp.close()
        print("%s downloaded!" % self.file_name)

    def extract(self):
        print("Extracting file:%s" % self.file_name)
        tar = tarfile.open(name=self.file_name, mode="r:gz")
        tar.extractall()
        tar.close()
        print("%s extracted!" % self.file_name)
