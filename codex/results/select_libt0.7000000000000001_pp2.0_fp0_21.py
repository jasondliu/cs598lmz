import select

# 显示当前系统所有的打开的文件描述符
def display_all_open_files():
    # 获取当前系统所有的打开的文件描述符
    open_file_list = select.epoll() # select.epoll() 可以监控的限制是1024个文件描述符，系统支持的文件描述符为10240个
    # 设置一个字典，字典的key为文件描述符，value为文件名
    files_for_key = {}
    for key,value in open_file_list.__dict__.items():
        #
