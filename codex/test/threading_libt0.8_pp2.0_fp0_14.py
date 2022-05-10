import threading
threading.Thread(target=lambda: open(__file__)).start()

def create_file(body, name):
    return (
        '<!DOCTYPE html>'
        '<br><a href="{0}">{0}</a><br>{1}'.format(
            name, body
        )
    )

class Directory:
    def __init__(self, path):
        self.path = path
        self.extensions = {
            'html': 'text/html',
            'css': 'text/css',
            'png': 'image/png'
        }
        self.view_files = (
            '403.html', '404.html', '.htaccess'
        )

    def get_content(self, path):
        if not path:
            path = 'index.html'
        if os.path.isfile(os.path.join(self.path, path)):
            extension = path.split('.')[1] if '.' in path else 'html'
