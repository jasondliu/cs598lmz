import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()
# ------------------------------------------------------------

# -----------------
# 相關函式定義區
# -----------------


def download_file(url, file_name):
    r = requests.get(url, stream=True)
    with open(file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return


def get_data(url):
    r = requests.get(url)
    return r.text


def get_json_data(url):
    r = requests.get(url)
    return r.json()


def post_data(url, payload):
    r = requests.post(url, data=payload)
    return r.text


def lineNotify(token, msg, picURI):
    url = "https://notify-api.line
