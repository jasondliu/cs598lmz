import ctypes
ctypes.windll.user32.LockWorkStation()

# 定义桌面路径
path = os.path.join(os.path.expanduser('~'), 'Desktop')
# 定义图片路径
img_path = os.path.join(path, 'wallpaper.jpg')


def download_wallpaper():
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    # 发送请求
    response = requests.get(url=url, headers=headers)
    # 获取图片
    img = response.content
    # 下载图片
    with open(img_path, 'wb') as f:
       
