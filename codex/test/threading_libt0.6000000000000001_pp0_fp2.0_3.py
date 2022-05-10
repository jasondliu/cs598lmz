import threading
threading.ThreadError

def upload_file(file):
    file_name = file.name
    file_data = file.read()
    file_size = len(file_data)
    file_crc = zlib.crc32(file_data)
    file_data = base64.b64encode(file_data)
    file_upload = {'name': file_name, 'data': file_data, 'size': file_size, 'crc': file_crc}
    file_upload = json.dumps(file_upload)

    headers = {'content-type': 'application/json'}
    r = requests.post('http://localhost:5000/upload', data=file_upload, headers=headers)
    print(r.json())

def download_file(file_name):
    file_download = {'name': file_name}
    file_download = json.dumps(file_download)
    headers = {'content-type': 'application/json'}
