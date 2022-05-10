import io
class File(io.RawIOBase):
    def __init__(self, path):
        self._path = path

    def read(self, size=-1):
        with open(self._path, 'rb') as f:
            return f.read(size)

    def readable(self):
        return True

class HttpResponse(object):
    def __init__(self, data, status_code=200, headers=None):
        self._data = data
        self._status_code = status_code
        self._headers = headers or {}

    def get_data(self):
        if isinstance(self._data, File):
            return self._data.read()
        return self._data

    def get_status_code(self):
        return self._status_code

    def get_headers(self):
        return self._headers

class HttpRequest(object):
    def __init__(self, method, path, headers, body):
        self._method = method
        self._path = path
        self._headers = headers
        self._body = body

    def get_method(self):
       
