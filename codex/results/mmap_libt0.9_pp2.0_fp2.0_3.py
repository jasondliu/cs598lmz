import mmap
import requests
import urllib.parse
#定义BASE_DIR方法
BASE_DIR = os.path.dirname(os.path.dirname(__file__))+os.sep
def upload_vuln_scan_file(filename):
    """
    上传漏洞扫描文件到网盘
    :param filename:
    :return:
    """
    upload_file_path = BASE_DIR+'uploaded_files'
    makeDirCreate(upload_file_path)
    filepath = upload_file_path+os.sep+filename
    print(filepath)
    api = 'https://pcs.baidu.com/rest/2.0/pcs/file?method=upload&type=tmpfile&access_token='
    app_key = "W8Qv0X10q3tE4Z4HwW8GvFRF"
    secret_key = "Sbt0l5h5X9MMOSG5
