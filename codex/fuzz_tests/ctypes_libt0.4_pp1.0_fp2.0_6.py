import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Kongregate Bot")

print("Kongregate Bot")
print("By: TheMrIron2")
print("")

username = input("Enter username: ")
password = input("Enter password: ")

print("")

print("Logging in...")

session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Upgrade-Insecure-Requests': '1'
