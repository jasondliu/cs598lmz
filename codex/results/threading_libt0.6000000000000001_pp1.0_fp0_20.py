import threading
threading.thread(target=run, args=())

# 프로그램 시작
app.run(host='0.0.0.0', port=80, debug=False)
