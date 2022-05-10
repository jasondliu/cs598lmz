import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

#需要填写你的 Access Key 和 Secret Key
access_key = '******'
secret_key = '******'

#构建鉴权对象
q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = '******'

#上传到七牛后保存的文件名
key = 'my-python-logo.png'

#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)

#要上传
