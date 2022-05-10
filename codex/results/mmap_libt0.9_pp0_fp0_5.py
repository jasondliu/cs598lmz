import mmap


def iterate_csv(file_name):
    try:
        with open(file_name) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                yield row
    except IOError:
        print('Could not open file: ', file_name)


class MyHandler(SimpleHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super(MyHandler, self).__init__(request, client_address, server)

        self.data_file = None

        # caches, store file data structures
        self.row_by_id_cache = {}

    def do_GET(self):
        if self.path == '/hello':
            header = "Content-Type: text/plain"
            f = BytesIO()
            f.write(b"Hello, world!\r\n")
            f.seek(0)

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("
