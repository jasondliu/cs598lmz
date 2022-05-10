import lzma
lzma.decompress()

def decompress_7z(file_name, password=None, output_dir=None, output_name=None):
    """
    解压缩7z文件
    :param file_name: 压缩包文件名
    :param password : 密码
    :param output_dir: 解压后文件存放目录
    :param output_name: 解压后文件存放目录
    :return:
    """
    try:
        if not output_dir:
            output_dir = os.path.dirname(file_name)
        if not output_name:
            output_name = os.path.basename(file_name)
        output_name = output_name.split('.')[0]
        output_name = os.path.join(output_dir, output_name)
        if not os.path.exists(output_name
