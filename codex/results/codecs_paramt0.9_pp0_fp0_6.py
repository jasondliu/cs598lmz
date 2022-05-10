import codecs
codecs.register_error('surrogate_or_unsafe', codecs.surrogateescape)

my_cd_dir = 'C:\\Users\\91239\\Downloads\\cd-rip'
my_cd_disk = 'C:\\Users\\91239\\Downloads\\'

#从一系列文件名中提取出数字 ID ，这些编号会在标题下一行出现。
#如果文件名没有编号 ID ，这个函数就会返回“999” ，这样我们就可以按照预期的顺序将它们排序
def track_id(s):
    pattern = r'^(\d{3})'
    result = re.search(pattern, s)
    if result:
