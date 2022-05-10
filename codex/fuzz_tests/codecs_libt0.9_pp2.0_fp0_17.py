import codecs
codecs.encode(a, 'base64')
array('b', [
    # 資料來源: https://tools.ietf.org/html/rfc4648
    # 常用於 X509 憑證轉換
    # 使用 encode('base64') 與 decode('base64') 方法
    # https://docs.python.org/3/library/functions.html#int.from_bytes
    int.from_bytes(
        "Man".encode('utf-8'), 'littl
