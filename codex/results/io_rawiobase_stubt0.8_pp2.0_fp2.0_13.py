import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b"Mocked bytes"


def mock_open(mock=None, data=None):
    if mock is None:
        mock = unittest.mock.Mock(spec=File)

    handle = unittest.mock.Mock(spec=File)
    handle.write.return_value = None
    if data is None:
        handle.__enter__.return_value = handle
        handle.read.return_value = b""
    else:
        handle.__enter__.return_value = data
    mock.return_value = handle
    return mock

class TestResponse(unittest.TestCase):
    def test_init(self):
        with mock_open() as mocked_open:
            with mock.patch('io.open', mocked_open):
                response = Response(filename='test.txt',
                                    data='<xml></xml>')

        self.assertEqual(response.filename, 'test.txt')
        self.assertEqual(response.data, '<xml
