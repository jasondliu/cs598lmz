import _struct

def get_mime_type(file_path):
    with open(file_path, 'rb') as f:
        data = f.read(24)
    if len(data) < 24:
        return None
    if data[:8] == '\211PNG\r\n\032\n':
        return 'image/png'
    if data[:4] == '\211PNG':
        return 'image/png'
    if data[6:10] in ('JFIF', 'Exif'):
        return 'image/jpeg'
    if data[:3] == 'GIF':
        return 'image/gif'
    if data[:4] == '\x89PNG':
        return 'image/png'
    if data[:2] == 'BM':
        return 'image/bmp'
    if data[:4] == '\x00\x00\x01\x00':
        return 'image/vnd.microsoft.icon'
    return None

