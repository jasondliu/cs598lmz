import codecs
codecs.register_error('myerror',MyError)

x=codecs.open("myfile.txt","r","utf-8","replace",errors="myerror")
