import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['UPLOAD_PATH'] = '../data/'

# 设置图片上传访问入口，指定一个虚拟路径/upload，在app下面/static/upload
app.config["UPLOADED_PHOTOS_DEST"] = "static/upload"
# 实例化UploadSet，并指定模式为图片
photos = UploadSet("photos", IMAGES)
# 配置文件上传属性，并指定允许上传的文件模式
app.config["UPLOADED_FIL
