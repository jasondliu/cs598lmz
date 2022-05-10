import mmap
import os
from prettytable import PrettyTable


class FileTools:
    def __init__(self):
        pass

    def search_file(self, directory, filename):
        '''
        递归查找文件
        :param directory: 查找的目录
        :param filename: 查找的文件名
        :return: 如果没找到，返回[], 如果找到了文件，返回list
        '''
        filelist = []
        for root, subdirs, files in os.walk(directory):
            if not subdirs and not files:
                return filelist
            else:
                for file in files:
                    if file == filename:
                        filelist.append(os.path.join(root, file))
                for subdir in subdirs:
                    filelist.extend(self.search_file(subdir, filename))
       
