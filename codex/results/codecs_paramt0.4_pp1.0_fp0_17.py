import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_file_info(filename):
    filename = filename.strip()
    if filename.startswith('http://'):
        return 'http', filename[len('http://'):]
    elif filename.startswith('https://'):
        return 'https', filename[len('https://'):]
    elif filename.startswith('file://'):
        return 'file', filename[len('file://'):]
    elif filename.startswith('ftp://'):
        return 'ftp', filename[len('ftp://'):]
    elif filename.startswith('ftps://'):
        return 'ftps', filename[len('ftps://'):]
    elif filename.startswith('sftp://'):
        return 'sftp', filename[len('sftp://'):]
    elif filename.find(':') > 0:
        return filename.split(':', 1)
    else:
        return 'file', filename

def _get
