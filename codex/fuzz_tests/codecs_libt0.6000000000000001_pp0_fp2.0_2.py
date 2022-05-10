import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接MySQL
import pymysql

app = Flask(__name__)
app.secret_key = "jfiegb"

# 连接MySQL
db = pymysql.connect(host="localhost", port=3306, user="root", password="", db="main", charset='utf8mb4')
cursor1 = db.cursor()

# 登录验证
# @app.before_request
# def check_login():
#     url = request.url
#     if url.endswith("/register") or url.endswith("/login") or url.endswith("/static/"):
#         return None
#     user_name = session.get("user_name")
#     if not user_name:
#         return redirect("/login")

# 登录页面
@app.route("/
