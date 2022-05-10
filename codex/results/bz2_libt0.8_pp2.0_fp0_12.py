import bz2
bz2File = bz2.BZ2File(fileUrl)
fileSize = bz2File.seek(0, 2)

decompressor = bz2.BZ2Decompressor()
done = 0

for i in range(int(fileSize / 10)):
    bz2File.seek(0)
    bz2File.seek(int(i * fileSize / 10))
    url = bz2File.readline()[:-1].decode("utf-8")
    curl = bz2File.readline()[:-1].decode("utf-8")

    if url != " " and curl != " ":
        urlId = db.url.find_one({"url": url})
        if urlId is None:
            urlId = db.url.insert_one({"url": url}).inserted_id
        else:
            urlId = urlId["_id"]

        curlId = db.url.find_one({"url": curl})
        if curlId is None:
            curlId = db.url.insert_one
