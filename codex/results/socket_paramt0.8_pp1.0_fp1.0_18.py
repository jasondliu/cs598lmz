import socket
socket.if_indextoname('4')

```

## 5.4 抓取网络数据

现在，我们有了基本的网络编程的工具，我们可以抓取一些网络数据了。

下面是一个简单的例子，用于抓取名叫 wu-tang 在 GitHub 上的所有项目。

```
# 安装依赖包
pip install requests

# 抓取网络数据
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}

