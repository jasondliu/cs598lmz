import codecs
codecs.register(lambda name:'idna'if name=='idna'else None)

#参数
geturl=input('输入起始网址:')
#====================================TXT模块初始化====================================
#TXT页面
TXT_area_path='./temp/'+str(geturl.replace('.',''))+'_TXT_area.txt'
TXT_pic_path='./temp/'+str(geturl.replace('.',''))+'_TXT_pic.txt'
TXT_file_path='./temp/'+str(geturl.replace('.',''))+'_TXT_file.txt'
TXT_info_path='./temp/'+str(geturl.replace('.',''))+'_TXT_info.txt'
#TXT_area 初始化
if not os.path.isfile(TXT_area_path):
    with open(TXT_area
