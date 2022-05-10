import bz2
# Test BZ2Decompressor on the file
with open("file.bz2", 'rb') as compressed:
    decompressor = bz2.BZ2Decompressor()
    with open("file_uncompressed.txt", 'wb') as uncompressed:
        firstTimestamp = 0
        delimiter = ","
        keysToWrite = ['timestamp', 'name', 'action_timestamp', 'action_user', 'action_text']
        toWriteCsv = csv.DictWriter(uncompressed, keysToWrite, delimiter=delimiter)
        toWriteCsv.writeheader()
        for rawData in iter(lambda: compressed.read(100*1024), b''):
            data = decompressor.decompress(rawData)
            if data:
                jsonData = json.loads(data)
                if jsonData['action'] == "edited":
                    csvToWrite = {}
                    csvToWrite['timestamp'] = jsonData['timestamp']
                    csvToWrite['name'] = jsonData['name']
                    csvToWrite['action_timestamp'] = jsonData['
