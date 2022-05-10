import socketserver
import time

sys.path.append('..')


class MHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("connected from:", self.client_address)
        # self.request.close()
        db_conn = sqlite3.connect("work.sql")
        data = self.request.recv(102400)
        if not data: break
        req = pickle.loads(data)
        ack = pickle.dumps('received ' + str(req))
        self.request.send(ack)
        print(req)
        cursor = db_conn.cursor()
        cursor.execute("select case when max(id) is null then 1 else max(id)+1 end from test;")
        id = cursor.fetchone()[0]
        cursor.execute("insert into test values(?, ?, ?);", (id, req['name'], req['state']))
        time.sleep(int(req['state']))
        cursor.execute("update test set end_at = datetime('now') where id
