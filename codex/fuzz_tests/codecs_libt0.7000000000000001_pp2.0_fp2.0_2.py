import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

########################################################################################################################


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class GetInfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("haha")

    def post(self):
        args = self.request.arguments
        json_str = self.get_argument("json", "")
        json_obj = json.loads(json_str)
        user = json_obj['user']
        passwd = json_obj['passwd']
        data = json_obj['data']
        if not (user == "" or passwd == ""):
            conn = pymysql.connect(host='127.0.0.1', port=3306, user=user, passwd=passwd, db='mysql')
            cursor = conn.cursor()
            if not data == "":
                if data == 'school
