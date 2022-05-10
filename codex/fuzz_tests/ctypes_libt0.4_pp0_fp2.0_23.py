import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("PySocks Proxy")

# импортируем модуль
import socks

# подключаемся к серверу
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

# проверяем соединение
print(requests.get('http://httpbin.org/ip').text)

# настраиваем прокси
proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

# проверяем соединение
print(requests.
