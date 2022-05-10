import threading
threading.Thread(target=lambda: importlib.import_module('dis')).start()
c = 1
while c<=10:
    time.sleep(2)
    c += 1
    now = datetime.datetime.now()
    print(now)
    threading.Thread(target=lambda: importlib.import_module('dis')).start()
importlib.reload(dis)


dic = {'이순신': '010-6666-7777',
       '강감찬': '010-7777-8888',
       '을지문덕': '010-8888-6666'}

print(dic)


dic = {'이순신': {'나이': 27, '성별': '남자', '핸드폰번호': '010-000000'},
       '강감찬': {'나이':
