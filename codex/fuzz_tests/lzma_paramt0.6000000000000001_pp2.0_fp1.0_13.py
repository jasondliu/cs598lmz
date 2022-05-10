from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 下载文件
def download_file(url, local_filename):
    r = requests.get(url)
    with open(local_filename, 'wb') as f:
        f.write(r.content)
download_file('http://httpbin.org/response-headers', 'response-headers.txt')

# 使用代理
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
requests.get("http://example.org", proxies=proxies)

# 利用SSL证书验证
requests.get('https://github.com', verify=True)
