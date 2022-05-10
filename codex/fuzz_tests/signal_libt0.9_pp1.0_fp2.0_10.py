import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from multiprocessing import Process
import os
from datetime import datetime

class pyastop:

    name = 'defualt'

    #작업 결과 기록 정보
    __scrap_url = None    #수집하려는 url
    __data_name = None    #추출하려는 항목 이름
    __dir_name = None     #추출하려는 항목의 파일이름
    __html_uri = None     #수집한 url 저장할 html 이름
    __html_cont = None    #수집한 url 저장할 html 내
