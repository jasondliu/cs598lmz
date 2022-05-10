import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'rb')

    def read(self, size=-1):
        return self.file.read(size)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def close(self):
        return self.file.close()

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

def upload(file_name):
    url = 'https://api.telegram.org/bot'+token+'/sendDocument'
    files = {'document': open(file_name, 'rb')}
    data = {'chat_id' : chat_id}
    r= requests.post(url, files=files, data=data)
    print(r.status_code, r
