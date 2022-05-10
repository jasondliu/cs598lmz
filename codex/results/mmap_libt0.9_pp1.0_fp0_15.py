import mmap

#namedtuple表示含有命名字段的元组
#https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000

# 可以参考https://tiobe.com/tiobe-index/ 
Language_Index = namedtuple("Language_Index", ['rank', 'rating', 'change', 'programmingLanguage'])

# 利用shutil自带的copyfile方法将csv文件复制到当前工作目录下
csv_url = 'https://www.tiobe.com/tiobe-index/'
csv_file_name = '/tmp/tiobe.csv'
if not os.path.exists(csv_file_name):
	print("no source file
