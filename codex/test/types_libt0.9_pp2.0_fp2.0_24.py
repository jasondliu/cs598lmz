import types
types.ClassType
class File:
    def __init__(self, name, menu_folder):
        self.__name = name
        self.__menu_folder = menu_folder
        self.__menu_folder.add(self)

    def get_name(self):
        return self.__name

    def get_menu_folder(self):
        return self.__menu_folder

class Menu_folder:
    def __init__(self, name, root):
        self.__name = name
        self.__root = root
        self.__root.add(self)

    def add(self, f):
        self.__root.add(f, self)

    def get_name(self):
        return self.__name
        
class Root:
    def __init__(self):
        self.__files = []
        self.__menu_folders = []
        self.__subfiles = {}
        self.__submenu_folders = {}
