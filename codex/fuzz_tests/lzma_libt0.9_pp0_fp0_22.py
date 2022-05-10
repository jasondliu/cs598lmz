import lzma
lzmac = lzma.LZMACompressor()

def init():
    global path, bucket, key_name, data
    path = '/Users/cyan/Downloads/rawdata/'
    bucket = 'result-netease'
    key_name = '/rawdata/'
    data = [f for f in listdir(path) if isfile(join(path, f))]


def put_file(filename):
    print filename
    foobar = open(path + '/' + filename, 'rb')
    resp = requests.delete(url=dedup_delete + filename[:-4], headers=header1)
    print resp.status_code
    print resp.content
    block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
    data = foobar.read()
    resp = block_blob_service.create_blob_from_bytes(bucket, key_name + filename, data, content_encoding='gzip', content_settings=ContentSettings(content_language='en') )

